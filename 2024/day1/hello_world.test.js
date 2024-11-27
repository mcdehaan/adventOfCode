import { test, expect } from "bun:test";
import { sayHello } from "./hello_world.js";

test('sayHello function should return "Hello, World!"', () => {
    expect(sayHello()).toBe("Hello, World!");
});
