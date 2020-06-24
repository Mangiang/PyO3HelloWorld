extern crate pyo3;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod HelloWorld;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn hello() -> PyResult<()> {
    HelloWorld::hello();
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule(hello_world)]
fn init(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(hello))?;

    Ok(())
}