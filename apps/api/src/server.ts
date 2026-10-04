import express from "express";
import { ping } from "./index";
import { config } from "./config";

const app = express();
app.use(express.json());

app.get("/health", (_req, res) => {
  res.json({ ok: true, service: "api", env: config.env });
});

app.get("/search-status", (_req, res) => {
  res.json({ ok: true, message: ping() });
});

app.listen(config.port, () => {
  console.log(`API listening on port ${config.port}`);
});
