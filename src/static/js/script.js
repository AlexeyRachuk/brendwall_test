document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('guitarForm');
    const tableBody = document.querySelector('#guitarTable tbody');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const text = document.getElementById('text').value;
        const price = document.getElementById('price').value;

        const csrftoken = getCookie('csrftoken');

        const response = await fetch('/api/guitars/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ name, text, price })
        });

        if (response.ok) {
            await fetchGuitars();
            form.reset();
        } else {
            alert('Failed to add guitar');
        }
    });

    async function fetchGuitars() {
        const response = await fetch('/api/guitars/');
        const guitars = await response.json();

        tableBody.innerHTML = '';
        guitars.forEach(guitar => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${guitar.name}</td>
                <td>${guitar.text}</td>
                <td>${guitar.price}</td>
            `;
            tableBody.appendChild(row);
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    fetchGuitars();
});
