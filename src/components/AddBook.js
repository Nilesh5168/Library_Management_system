import { useState } from "react";
import api from "../api";

const AddBook = ({ onBookAdded }) => {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [isbn, setIsbn] = useState("");
  const [publishedDate, setPublishedDate] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/books/", { title, author, isbn, published_date: publishedDate });
      alert("Book added successfully!");
      setTitle("");
      setAuthor("");
      setIsbn("");
      setPublishedDate("");
      onBookAdded(); // Notify the parent to refresh the book list
    } catch (error) {
      console.error("Failed to add book", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
        placeholder="Title" 
        required 
      />
      <input 
        value={author} 
        onChange={(e) => setAuthor(e.target.value)} 
        placeholder="Author" 
        required 
      />
      <input 
        value={isbn} 
        onChange={(e) => setIsbn(e.target.value)} 
        placeholder="ISBN" 
        required 
      />
      <input 
        type="date" 
        value={publishedDate} 
        onChange={(e) => setPublishedDate(e.target.value)} 
        required 
      />
      <button type="submit">Add Book</button>
    </form>
  );
};

export default AddBook;
