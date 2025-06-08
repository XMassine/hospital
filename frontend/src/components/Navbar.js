import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#ececec" }}>
      <Link to="/" style={{ marginRight: "1rem" }}>Login</Link>
      <Link to="/dashboard" style={{ marginRight: "1rem" }}>Dashboard</Link>
      <Link to="/consultations" style={{ marginRight: "1rem" }}>Consultations</Link>
      <Link to="/history">History</Link>
    </nav>
  );
}

export default Navbar;
