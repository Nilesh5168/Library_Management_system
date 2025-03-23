import { Link, useNavigate } from "react-router-dom";
import { logout } from "../api";

const Navbar = () => {
  const navigate = useNavigate();
  const isAuthenticated = localStorage.getItem("access_token") !== null;

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav style={styles.navbar}>
      <div style={styles.spacer}></div> {/* Empty div for spacing */}
      <h2 style={styles.logo}>{isAuthenticated ? "Admin View" : "Student View"}</h2>
      <div>
        {isAuthenticated ? (
          <>
            <Link to="/dashboard" style={styles.link}>Dashboard</Link>
            <button onClick={handleLogout} style={styles.button}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login" style={styles.link}>Admin Login</Link>
            <Link to="/register" style={styles.link}>Register</Link>
          </>
        )}
      </div>
    </nav>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "10px 20px",
    backgroundColor: "#282c34",
    color: "white",
    position: "relative",
  },
  logo: {
    fontSize: "1.5rem",
    position: "absolute",
    left: "50%",
    transform: "translateX(-50%)",
  },
  link: {
    color: "white",
    textDecoration: "none",
    margin: "0 10px",
  },
  button: {
    backgroundColor: "#f44336",
    color: "white",
    border: "none",
    padding: "5px 10px",
    cursor: "pointer",
    marginLeft: "10px",
  },
  spacer: {
    width: "100px", // Just to keep alignment proper
  },
};

export default Navbar;
