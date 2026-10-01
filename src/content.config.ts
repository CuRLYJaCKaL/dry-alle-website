import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    // SERP basligi makale basligindan AYRI olabilir: uzun aciklayici
    // baslik okuyucu ve H1 icin iyi, Google 60 karakterden sonrasini kirpar.
    seoTitle: z.string().optional(),
    description: z.string(),
    date: z.string(),
    author: z.string().optional(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
    faq: z.array(z.object({ question: z.string(), answer: z.string() })).optional(),
  }),
});

export const collections = { blog };
