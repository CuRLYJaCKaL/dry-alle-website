// ─── Types ───
interface ValidationError {
  field: string;
  message: string;
}

// ─── Template Interpolation ───

/** SEO template interpolation — {token} → value */
export function interpolate(template: string, tokens: Record<string, string>): string {
  return template.replace(/\{(\w+)\}/g, (_, key) => tokens[key] ?? '');
}

// ─── Deterministic Variant Selection ───

/** Bolge sayfalari icin deterministic variant secimi — ayni slug her zaman ayni varyanti dondurur */
export function deterministicIndex(slug: string, arrayLength: number): number {
  if (arrayLength <= 0) return 0;
  let hash = 0;
  for (let i = 0; i < slug.length; i++) {
    hash = ((hash << 5) - hash) + slug.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash) % arrayLength;
}

// ─── Config Validation ───

/** Build-time config dogrulama — eksik zorunlu alan varsa build'i durdurur */
export function validateConfig(config: Record<string, unknown>): void {
  const errors: ValidationError[] = [];

  const requiredStrings = [
    'identity.businessName',
    'identity.sectorLabel',
    'identity.schemaType',
    'contact.phone',
    'contact.domain',
  ];

  for (const path of requiredStrings) {
    const value = path.split('.').reduce((obj: unknown, key) =>
      (obj as Record<string, unknown>)?.[key], config);
    if (!value || typeof value !== 'string') {
      errors.push({ field: path, message: 'Required string field is missing or empty' });
    }
  }

  const requiredArrays = ['services', 'serviceAreas'];
  for (const path of requiredArrays) {
    const value = path.split('.').reduce((obj: unknown, key) =>
      (obj as Record<string, unknown>)?.[key], config);
    if (!Array.isArray(value) || value.length === 0) {
      errors.push({ field: path, message: 'Required array is missing or empty' });
    }
  }

  if (!config.seoTemplates || typeof config.seoTemplates !== 'object') {
    errors.push({ field: 'seoTemplates', message: 'seoTemplates object is required' });
  } else {
    const requiredSeoKeys = ['homeTitle', 'serviceTitle', 'regionTitle', 'aboutTitle', 'catalogName'];
    for (const key of requiredSeoKeys) {
      if (!(config.seoTemplates as Record<string, unknown>)[key]) {
        errors.push({ field: `seoTemplates.${key}`, message: 'Required SEO template missing' });
      }
    }
  }

  const serviceNames = (config.services as Array<{name: string}>)?.map(s => s.name) ?? [];
  const duplicateServices = serviceNames.filter((n, i) => serviceNames.indexOf(n) !== i);
  if (duplicateServices.length > 0) {
    errors.push({ field: 'services', message: `Duplicate service names: ${duplicateServices.join(', ')}` });
  }

  if (errors.length > 0) {
    const report = errors.map(e => `  - ${e.field}: ${e.message}`).join('\n');
    throw new Error(`Config validation failed:\n${report}`);
  }
}
