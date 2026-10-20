#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevOps Demo Application
Assignment 6: Jenkins Integration with GitHub
"""

import sys
import datetime
import io

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

APP_NAME = "DevOps Jenkins Demo"
VERSION = "1.0.0"
AUTHOR = "DevOps Student"


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to {APP_NAME} v{VERSION}"


def get_build_info() -> dict:
    """Return basic build/runtime information."""
    return {
        "app": APP_NAME,
        "version": VERSION,
        "author": AUTHOR,
        "python_version": sys.version.split()[0],
        "build_time": datetime.datetime.now().isoformat(),
    }


def run_tests() -> bool:
    """Run simple unit tests inline."""
    print("\n[TEST] Running Tests...")
    passed = 0
    failed = 0

    # Test 1 – greet default
    result = greet()
    expected = f"Hello, World! Welcome to {APP_NAME} v{VERSION}"
    if result == expected:
        print("  [PASS] Test 1 PASSED: greet() default")
        passed += 1
    else:
        print(f"  [FAIL] Test 1 FAILED: got '{result}'")
        failed += 1

    # Test 2 – greet with name
    result = greet("Jenkins")
    if "Jenkins" in result:
        print("  [PASS] Test 2 PASSED: greet('Jenkins')")
        passed += 1
    else:
        print(f"  [FAIL] Test 2 FAILED: got '{result}'")
        failed += 1

    # Test 3 – build info keys
    info = get_build_info()
    required_keys = {"app", "version", "author", "python_version", "build_time"}
    if required_keys.issubset(info.keys()):
        print("  [PASS] Test 3 PASSED: get_build_info() keys")
        passed += 1
    else:
        print("  [FAIL] Test 3 FAILED: missing keys")
        failed += 1

    print(f"\n  Results: {passed} passed, {failed} failed")
    return failed == 0


def main():
    print("=" * 55)
    print(f"  {APP_NAME}")
    print(f"  Version : {VERSION}")
    print("=" * 55)

    # Print greeting
    print(f"\n{greet()}\n")

    # Print build info
    info = get_build_info()
    print("[INFO] Build Information:")
    for key, value in info.items():
        print(f"   {key:<18}: {value}")

    # Run tests
    all_passed = run_tests()

    print("\n" + "=" * 55)
    if all_passed:
        print("  BUILD SUCCESSFUL -- All tests passed!")
    else:
        print("  BUILD FAILED -- Some tests did not pass.")
        sys.exit(1)
    print("=" * 55)


if __name__ == "__main__":
    main()
