import { useState, useEffect } from "react";
import api from "../api";

const BookList = () => {
  const [books, setBooks] = useState([]);
  const [editingBook, setEditingBook] = useState(null);
  const [updatedData, setUpdatedData] = useState({
    title: "",
    author: "",
    isbn: "",
    published_date: "",
  });

  // Fetch books on page load
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

  // Handle Edit Click
  const handleEditClick = (book) => {
    setEditingBook(book.id);
    setUpdatedData({
      title: book.title,
      author: book.author,
      isbn: book.isbn,
      published_date: book.published_date,
    });
  };

  // Handle Update (PUT)
  const handleUpdate = async (bookId) => {
    try {
      await api.put(`/books/${bookId}/`, updatedData);
      setEditingBook(null);
      fetchBooks(); // Refresh the book list
      alert("Book updated successfully!");
    } catch (error) {
      console.error("Error updating book", error);
    }
  };

  // Handle Delete (DELETE)
  const handleDelete = async (bookId) => {
    try {
      await api.delete(`/books/${bookId}/`);
      fetchBooks(); // Refresh the book list
    } catch (error) {
      console.error("Error deleting book", error);
    }
  };

  return (
    <div>
      <h2>Book List</h2>
      {books.length > 0 ? (
        <table border="1" cellPadding="10" cellSpacing="0">
          <thead>
            <tr>
              <th>Title</th>
              <th>Author</th>
              <th>ISBN</th>
              <th>Published Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {books.map((book) => (
              <tr key={book.id}>
                {editingBook === book.id ? (
                  <>
                    <td>
                      <input
                        type="text"
                        value={updatedData.title}
                        onChange={(e) => setUpdatedData({ ...updatedData, title: e.target.value })}
                      />
                    </td>
                    <td>
                      <input
                        type="text"
                        value={updatedData.author}
                        onChange={(e) => setUpdatedData({ ...updatedData, author: e.target.value })}
                      />
                    </td>
                    <td>
                      <input
                        type="text"
                        value={updatedData.isbn}
                        onChange={(e) => setUpdatedData({ ...updatedData, isbn: e.target.value })}
                      />
                    </td>
                    <td>
                      <input
                        type="date"
                        value={updatedData.published_date}
                        onChange={(e) => setUpdatedData({ ...updatedData, published_date: e.target.value })}
                      />
                    </td>
                    <td>
                      <button onClick={() => handleUpdate(book.id)}>Save</button>
                      <button onClick={() => setEditingBook(null)}>Cancel</button>
                    </td>
                  </>
                ) : (
                  <>
                    <td>{book.title}</td>
                    <td>{book.author}</td>
                    <td>{book.isbn}</td>
                    <td>{book.published_date}</td>
                    <td>
                      <button onClick={() => handleEditClick(book)}>Update</button>
                      <button onClick={() => handleDelete(book.id)}>Delete</button>
                    </td>
                  </>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No books available</p>
      )}
    </div>
  );
};

export default BookList;
