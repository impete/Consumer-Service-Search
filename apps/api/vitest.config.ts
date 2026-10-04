import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,
    include: ["../../tests/{unit,integration}/**/*.test.ts"],
    reporters: ["default", "junit"],
    outputFile: { junit: "../../reports/api-junit.xml" },
    coverage: {
      provider: "v8",
      include: ["src/**"],
      reportsDirectory: "../../reports/api-coverage",
      reporter: ["text", "lcov"],
    },
  },
});
