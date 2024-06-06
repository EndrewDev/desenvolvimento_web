// script.js
document.addEventListener('DOMContentLoaded', () => {
    const bookForm = document.getElementById('new-book-form');
    const bookList = document.getElementById('books');

    bookForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;
        const publicationDate = document.getElementById('publication-date').value;
        const description = document.getElementById('description').value;

        const bookItem = document.createElement('li');
        bookItem.innerHTML = `
            <h3>${title}</h3>
            <p><strong>Autor:</strong> ${author}</p>
            <p><strong>Data de Publicação:</strong> ${publicationDate}</p>
            <p><strong>Descrição:</strong> ${description}</p>
        `;

        bookList.appendChild(bookItem);

        bookForm.reset();
    });
});