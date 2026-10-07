// REQ-0001
describe("buildSearchRequest", () => {
  it("applies defaults", async () => {
    const { buildSearchRequest } = await import("../../../apps/api/src/index");
    expect(buildSearchRequest({})).toEqual({
      serviceType: "service",
      location: "unknown",
      radiusMiles: 5,
      priority: "score",
    });
  });
});
