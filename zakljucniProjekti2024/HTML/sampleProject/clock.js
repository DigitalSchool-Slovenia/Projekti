function updateClock() {
    const now = new Date();
    const hour = now.getHours() % 12;
    const minute = now.getMinutes();
    const second = now.getSeconds();

    const hourHand = document.getElementById('hourClock');
    const minuteHand = document.getElementById('minuteClock');
    const secondHand = document.getElementById('secondClock');

    const hourDeg = (hour * 30) + (0.5 * minute); // 30 degrees per hour, 0.5 degrees per minute
    const minuteDeg = (minute * 6) + (0.1 * second); // 6 degrees per minute, 0.1 degrees per second
    const secondDeg = second * 6; // 6 degrees per second

    hourHand.style.transform = `rotate(${hourDeg}deg)`;
    minuteHand.style.transform = `rotate(${minuteDeg}deg)`;
    secondHand.style.transform = `rotate(${secondDeg}deg)`;
}

// Initial call to update the clock when the page loads
updateClock();

// Update the clock every second
setInterval(updateClock, 1000);
