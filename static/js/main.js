const main = () => {
    let score = 0;
    const power = document.getElementById('power');
    power.addEventListener('click', () => {
        // main button action here
    })

    const buttons = document.getElementsByClassName('filter');
    [...buttons].forEach(btn => {
        btn.addEventListener('click', () => {
            btn.classList.remove("filter");
            score += +btn.textContent;
        })
    });

    const randomInteger = (min, max) => {
        let rand = min + Math.random() * (max + 1 - min);
        return Math.floor(rand);
    }

    const action = () => {
        const buttons = [...document.getElementsByClassName('filter')];
        if (buttons.length > 0) {
            buttons.forEach(btn => {
                btn.style.visibility = "hidden";
            });
            const visibleIndex = randomInteger(0, buttons.length - 1);
            buttons[visibleIndex].style.visibility = "visible";
        } else {
            power.textContent = +power.textContent + score;
            score = 0;
            const buttons = [...document.getElementsByClassName('boost')];
            buttons.forEach(btn => {
                btn.classList.add("filter");
                btn.style.visibility = "hidden";
            });
        }
    }

    const timerId = setInterval(action, 2000);
}

window.onload = main;