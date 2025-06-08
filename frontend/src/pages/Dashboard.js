import React, { useEffect, useState } from "react";

function Dashboard() {
  const [patients, setPatients] = useState([]);
  const [newPatient, setNewPatient] = useState({ name: "", age: "", email: "" });

  useEffect(() => {
    fetch("http://localhost:8000/patients")
      .then((res) => res.json())
      .then((data) => setPatients(data));
  }, []);

  const addPatient = async () => {
    await fetch("http://localhost:8000/patients", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newPatient),
    });
    window.location.reload();
  };

  return (
    <div>
      <h2>Patients</h2>
      <input placeholder="Name" onChange={e => setNewPatient({...newPatient, name: e.target.value})} />
      <input placeholder="Age" onChange={e => setNewPatient({...newPatient, age: parseInt(e.target.value)})} />
      <input placeholder="Email" onChange={e => setNewPatient({...newPatient, email: e.target.value})} />
      <button onClick={addPatient}>Add Patient</button>

      <ul>
        {patients.map((p, i) => (
          <li key={i}>{p.name} – {p.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
