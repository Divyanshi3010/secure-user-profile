import API from "../api";
import { useEffect, useState } from "react";

export default function Dashboard() {
  const [profile, setProfile] = useState({});

  useEffect(() => {
    API.get("/profile").then(res => setProfile(res.data));
  }, []);

  return (
    <div>
      <h3>{profile.email}</h3>
      <p>Aadhaar: {profile.aadhaar}</p>
    </div>
  );
}
