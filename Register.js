import { useState } from "react";
import API from "../api";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [aadhaar, setAadhaar] = useState("");
  const [msg, setMsg] = useState("");

  const register = async () => {
    try {
      const res = await API.post("/register", {
        email,
        password,
        aadhaar
      });

      setMsg(res.data.msg);
    } catch (err) {
      setMsg(err?.response?.data?.error || "Registration failed. Try again.");
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <input
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />

      <input
        placeholder="Aadhaar / ID"
        value={aadhaar}
        onChange={e => setAadhaar(e.target.value)}
      />

      <button onClick={register}>Register</button>

      {msg && <p>{msg}</p>}
    </div>
  );
}
