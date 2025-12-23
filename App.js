import { useState } from "react";
import Login from "./components/Login";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!localStorage.getItem("token")
  );

  return (
    <div style={{ padding: "20px" }}>
      <h1>Secure User Profile System</h1>

      {!isLoggedIn ? (
        <>
          <Register />
          <hr />
          <Login onLogin={() => setIsLoggedIn(true)} />
        </>
      ) : (
        <Dashboard onLogout={() => setIsLoggedIn(false)} />
      )}
    </div>
  );
}

export default App;
