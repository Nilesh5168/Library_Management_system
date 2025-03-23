import { useState } from "react";
import api from "./api";

const UpdateBook = ({ bookId, existingTitle, existingAuthor, onUpdate }) => {
  const [title, setTitle] = useState(existingTitle);
  const [author, setAuthor] = useState(existingAuthor);

  const handleUpdate = async (e) => {
    e.preventDefault();
    try {
      await api.put(`/books/update/${bookId}/`, { title, author });
      alert("Book updated successfully!");
      onUpdate();
    } catch (error) {
      console.error("Error updating book", error);
    }
  };

  return (
    <form onSubmit={handleUpdate}>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" required />
      <input value={author} onChange={(e) => setAuthor(e.target.value)} placeholder="Author" required />
      <button type="submit">Update Book</button>
    </form>
  );
};

export default UpdateBook;
