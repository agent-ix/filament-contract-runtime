//! RT acceptance of FSV's checked unit graph and normalized compound units.
#![cfg(feature = "exact")]

use filament_semantic_value::unit::UnitGraph;
use ix_trace_rs::trace;
use std::collections::BTreeMap;

#[trace("TC-035", "FR-007-AC-13")]
#[test]
fn tc_035_fsv_compound_unit_debug_names_every_boxed_field() {
    let graph = UnitGraph::from_checked_nodes(&BTreeMap::new(), &BTreeMap::new()).unwrap();
    let dimensionless = graph.compound_unit(&[]).unwrap();
    assert_eq!(
        format!("{dimensionless:?}"),
        "CompoundUnit { terms: {}, dimension: Dimension({}) }"
    );
}
