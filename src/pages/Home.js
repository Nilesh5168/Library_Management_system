import { useEffect, useState } from "react";
import api from "../api";
import BookList from "../components/BookList";

const Home = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await api.get("/books/");
      setBooks(response.data);
    } catch (error) {
      console.error("Error fetching books", error);
    }
  };

  return (
    <div>
      <h2>Library Books</h2>
      <BookList books={books} setBooks={setBooks} />
    </div>
  );
};

export default Home;
