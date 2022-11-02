const button = document.getElementById('post-reads-btn');
const input = document.getElementById('post-reads-input');
const links = input.value();

button.addEventListener('click', async _ => {
    try {     
        const responsePost = await fetch('/reads', {
            method: 'post',
            body: {
                "links": links,
            }
        });
        console.log('Completed!', responsePost, responseGet);
    } catch(err) {
        console.error(`Error: ${err}`);
    }
});