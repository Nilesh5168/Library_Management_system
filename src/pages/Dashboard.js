import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api, { logout } from "../api";
import AddBook from "../components/AddBook";
import BookList from "../components/BookList";

const Dashboard = () => {
  const [token, setToken] = useState(localStorage.getItem("access_token"));
  const [books, setBooks] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate("/login"); // Redirect to login if not authenticated
    } else {
      fetchBooks(); // Fetch books initially
    }
  }, [token, navigate]);

  const fetchBooks = async () => {
    try {
      const response = await api.get("/books/");
      setBooks(response.data);
    } catch (error) {
      console.error("Error fetching books", error);
    }
  };

  const handleLogout = () => {
    logout();
    setToken(null);
    navigate("/login");
  };

  return (
    <div>
      <h2>Library Dashboard</h2>
      <button onClick={handleLogout}>Logout</button>
      <AddBook onBookAdded={fetchBooks} />
      <BookList books={books} setBooks={setBooks} />
    </div>
  );
};

export default Dashboard;
