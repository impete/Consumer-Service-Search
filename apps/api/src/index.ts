export type SearchRequest = {
  serviceType: string;
  location: string;
  radiusMiles: number;
  priority: string;
};

export const ping = () => ({ ok: true, service: "api" });

export const buildSearchRequest = (input: Partial<SearchRequest>): SearchRequest => ({
  serviceType: input.serviceType || "service",
  location: input.location || "unknown",
  radiusMiles: input.radiusMiles || 5,
  priority: input.priority || "score",
});
