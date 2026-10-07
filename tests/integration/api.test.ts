// REQ-0001
import type { AddressInfo } from "node:net";

describe("api routes", () => {
  let server: import("node:http").Server;
  let base: string;

  beforeAll(async () => {
    const { app } = await import("../../apps/api/src/app");
    server = app.listen(0);
    base = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
  });

  afterAll(() => new Promise((resolve) => server.close(resolve)));

  it("GET /health", async () => {
    const body = await (await fetch(`${base}/health`)).json();
    expect(body.ok).toBe(true);
    expect(body.service).toBe("api");
  });

  it("GET /search-status @noncritical", async () => {
    const body = await (await fetch(`${base}/search-status`)).json();
    expect(body.ok).toBe(true);
  });
});
