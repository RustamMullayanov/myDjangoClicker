const main = () => {
    let boost = 0;
    const scoreDiv = document.getElementById('score');
    const powerDiv = document.getElementById('power');
    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value

    powerDiv.addEventListener('click', async () => {
        const power = +powerDiv.textContent;
        const score = +scoreDiv.textContent + power;
        scoreDiv.textContent = score.toString();
        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrftoken
            },
            credentials: 'same-origin',
            body: JSON.stringify({score, power})
        }
        try {
            const res = await fetch('/stat', options);
            console.log(await res.json());
        } catch (e) {
            console.error(e);
        }
    })

    const buttons = document.getElementsByClassName('filter');
    [...buttons].forEach(btn => {
        btn.addEventListener('click', () => {
            btn.classList.remove("filter");
            boost += +btn.textContent;
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
            powerDiv.textContent = +powerDiv.textContent + boost;
            boost = 0;
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