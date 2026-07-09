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

  // serviceAreaPages (lokasyon×hizmet combo) guard — anti-doorway + cakisma + tekillik
  const sap = config.serviceAreaPages;
  if (Array.isArray(sap)) {
    const areas = (config.serviceAreas as Array<{districtSlug: string; neighborhoods: Array<{slug: string}>}>) ?? [];
    const serviceSlugs = new Set(((config.services as Array<{slug: string}>) ?? []).map(s => s.slug));
    const seen = new Set<string>();
    sap.forEach((e: Record<string, unknown>, i: number) => {
      const d = e.districtSlug as string;
      const nh = e.neighborhoodSlug as string | undefined;
      const sv = e.serviceSlug as string;
      const area = areas.find(a => a.districtSlug === d);
      if (!area) errors.push({ field: `serviceAreaPages[${i}]`, message: `Unknown districtSlug: ${d}` });
      if (nh && area && !area.neighborhoods.some(n => n.slug === nh)) errors.push({ field: `serviceAreaPages[${i}]`, message: `neighborhoodSlug ${nh} not in ${d}` });
      if (!serviceSlugs.has(sv)) errors.push({ field: `serviceAreaPages[${i}]`, message: `Unknown serviceSlug: ${sv}` });
      // 2-segment cakisma: ilce duzeyi combo'da serviceSlug bir mahalle slug'i olamaz
      if (!nh && area && area.neighborhoods.some(n => n.slug === sv)) errors.push({ field: `serviceAreaPages[${i}]`, message: `serviceSlug ${sv} collides with a neighborhood in ${d}` });
      // anti-doorway: ozgun icerik zorunlu
      const intro = e.intro as string;
      const body = e.bodyParagraphs as unknown[];
      const faq = e.faq as unknown[];
      if (!intro || typeof intro !== 'string' || intro.length < 40) errors.push({ field: `serviceAreaPages[${i}]`, message: 'intro missing or too short (unique content required)' });
      if (!Array.isArray(body) || body.length < 1) errors.push({ field: `serviceAreaPages[${i}]`, message: 'bodyParagraphs required (>=1)' });
      if (!Array.isArray(faq) || faq.length < 3) errors.push({ field: `serviceAreaPages[${i}]`, message: 'faq required (>=3 unique Q&A)' });
      // kombinasyon tekilligi
      const key = `${d}/${nh ?? ''}/${sv}`;
      if (seen.has(key)) errors.push({ field: `serviceAreaPages[${i}]`, message: `Duplicate combo: ${key}` });
      seen.add(key);
    });
  }

  if (errors.length > 0) {
    const report = errors.map(e => `  - ${e.field}: ${e.message}`).join('\n');
    throw new Error(`Config validation failed:\n${report}`);
  }
}
