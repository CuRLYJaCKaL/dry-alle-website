// Extract ev-tekstili services without images
const fs = require('fs');

// Read the pricing data file
const data = fs.readFileSync('/Users/macos/Documents/Projeler/DryAlle/js/pricing-data.js', 'utf8');

// Extract the array content
const arrayMatch = data.match(/const multiServicePricingData = \[([\s\S]*)\];/);
if (!arrayMatch) {
  console.log('Could not find pricing data array');
  process.exit(1);
}

// Parse the JavaScript array
let arrayContent = arrayMatch[1];

// Add proper JSON formatting
arrayContent = `[${arrayContent}]`;

// Clean up the content to make it valid JSON
arrayContent = arrayContent
  .replace(/\/\*[\s\S]*?\*\//g, '') // Remove block comments
  .replace(/\/\/.*$/gm, '') // Remove line comments
  .replace(/,\s*}/g, '}') // Remove trailing commas in objects
  .replace(/,\s*]/g, ']') // Remove trailing commas in arrays
  .replace(/(\w+):/g, '"$1":') // Quote object keys
  .replace(/'/g, '"'); // Replace single quotes with double quotes

try {
  const services = JSON.parse(arrayContent);
  
  // Filter ev-tekstili services
  const evTekstiliServices = services.filter(service => service.category === 'ev-tekstili');
  
  // Separate services with and without images
  const withImages = evTekstiliServices.filter(service => service.image);
  const withoutImages = evTekstiliServices.filter(service => !service.image);
  
  console.log(`Total ev-tekstili services: ${evTekstiliServices.length}`);
  console.log(`Services WITH images: ${withImages.length}`);
  console.log(`Services WITHOUT images: ${withoutImages.length}`);
  
  console.log('\n=== SERVICES WITH IMAGES ===');
  withImages.forEach(service => {
    console.log(`${service.id} - ${service.name} (${service.subcategory})`);
  });
  
  console.log('\n=== SERVICES WITHOUT IMAGES (ORGANIZED BY SUBCATEGORY) ===');
  
  const subcategories = {
    'hali-kilim': [],
    'yatak-takimi': [],
    'perde-tul': [],
    'mobilya-tekstili': []
  };
  
  withoutImages.forEach(service => {
    if (subcategories[service.subcategory]) {
      subcategories[service.subcategory].push(service);
    }
  });
  
  Object.keys(subcategories).forEach(subcategory => {
    if (subcategories[subcategory].length > 0) {
      console.log(`\n--- ${subcategory.toUpperCase()} (${subcategories[subcategory].length} services) ---`);
      subcategories[subcategory].forEach(service => {
        console.log(`${service.id} - ${service.name}`);
      });
    }
  });
  
} catch (error) {
  console.error('Error parsing data:', error.message);
  // Try to extract services manually using regex
  console.log('\nFallback: Using regex extraction...');
  
  const serviceMatches = data.match(/{[^}]*category:\s*"ev-tekstili"[^}]*}/g);
  if (serviceMatches) {
    console.log(`Found ${serviceMatches.length} ev-tekstili services with regex`);
  }
}