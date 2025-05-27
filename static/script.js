document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.emotion-btn');
    const verseDisplay = document.getElementById('verse-display');

    buttons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const emotion = btn.getAttribute('data-emotion');
            verseDisplay.textContent = 'Loading...';

            try {
                const response = await fetch(`/verse/${emotion}`);
                if (!response.ok) {
                    verseDisplay.textContent = 'Sorry, no verses found for this emotion.';
                    return;
                }
                const data = await response.json();

                verseDisplay.innerHTML = `
                    <p>"${data.text}"</p>
                    <p>${data.reference}</p>
                `;
            } catch (error) {
                verseDisplay.textContent = 'Error fetching verse. Try again later.';
                console.error(error);
            }
        });
    });
});
