---
id: TC-199
title: "Build the exact profile no_std and keep the default footprint"
type: TC
relationships:
  - target: ix://agent-ix/filament-contract-runtime/FR-275
    type: verifies
---
# TC-199: Build the exact profile no_std and keep the default footprint

## Description

Check that the runtime with `exact` and without `std` builds for `thumbv7em-none-eabi` against
`filament-exact` and `filament-semantic-value`, and that the default profile and its footprint measurement
do not resolve either shared crate or transitive `quire-canonical` crates.

## Test Procedure

0. Read the root package's declared `rust-version` in `Cargo.toml` as the compatibility
   floor (FR-275-AC-20). Inspect the feature and footprint gate recipes: each obtains
   its build compiler from `rust-toolchain.toml`.
1. Run the `make test-features` row `build-exact-no-std-msrv` (`exact`, no `std`, target
   `thumbv7em-none-eabi`) with the selected compiler; expect success (FR-006-AC-8,
   FR-275-AC-9). Run `make msrv` and expect the same selection (FR-275-AC-21).
   In a scratch copy, change `rust-version` to another supported floor and observe
   both `make msrv` and `make size` retain the selected compiler. Remove the floor
   or toolchain channel, or select an unavailable compiler, and observe both fail.
2. Run `make size`: after the build it lists the footprint graph with `cargo tree -p
   filament-contract-runtime-footprint --target thumbv7em-none-eabi` and fails when `filament-exact`,
   `filament-semantic-value`, `quire-canonical` or `quire-canonical-derive` is in it; expect it to
   report that the graph holds no shared exact dependency (FR-275-AC-10). Enabling `exact` on the
   footprint dependency in a scratch copy makes that listing contain those crates.
3. Run `make size`; expect `.text` plus `.rodata` inside NFR-001-AC-3's 500 byte to 4 KiB band and no
   panic relocation (FR-275-AC-11). Run `cargo test --locked --bin
   check_linked_footprint` for the report-parser controls: empty, malformed,
   foreign-only and core-only relocation populations fail as unavailable even
   with an in-band size report; recognized runtime/harness headers with no panic
   relocation pass. A similarly named foreign crate contributes neither linked
   bytes nor panic references. The retained-panic and both size-bound controls
   must also pass. These parser controls are partial evidence for this step;
   they do not establish the target build, compiler selection or dependency graph.
4. After AD-004 step 5, repeat the no-std target build on the selected compiler with the shared
   evaluation leaf and one generated-body consumer. Check the lock has one
   evaluation-leaf entry, and neither target graph resolves the FSL workspace
   source, an RT-local evaluator, or a compatibility alias. Run TC-194's
   checked-input and generated-body host cases with `std` disabled. Record the
   linked `measurement/evaluator` no_std executable for that target. Record
   the resulting ELF path and its `.text` plus `.rodata` sum from `llvm-size
   -A`. Run the FR-273-AC-13 deep case as a solitary native executable under
   `/usr/bin/time -v`; record the executable path and its `Maximum resident
   set size` in bytes after multiplying the reported KiB by 1024. Name both
   measurements and their commands in the receipt (FR-275-AC-29, AC-30).
5. Repeat `make size` after the leaf adoption; assert the default graph has no
   evaluation leaf, linked `.text` plus `.rodata` stays in its own 500-byte to
   4-KiB band, and the panic-relocation check passes. Report the exact-profile
   measurements separately without applying the default 4-KiB ceiling to
   them (FR-275-AC-30).

## Expected Results

The exact profile builds on the bare-metal target; the footprint graph holds no kernel and its band
is unchanged.
