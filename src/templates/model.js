const button = document.getElementById('post-question-btn');
const input = document.getElementById('post-question-input');
const question = input.value();

button.addEventListener('click', async _ => {
    try {     
        const responsePost = await fetch('/question', {
            method: 'post',
            body: {
                "question": question,
            }
        });
        console.log('Completed!', responsePost, responseGet);
    } catch(err) {
        console.error(`Error: ${err}`);
    }
});