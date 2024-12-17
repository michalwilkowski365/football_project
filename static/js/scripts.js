document.addEventListener("DOMContentLoaded", () => {
    const datesContainer = document.getElementById("dates");
    const matchesTable = document.getElementById("matches");

    // Generowanie kalendarza
    const generateDates = () => {
        const today = new Date();
        const dates = [];
        for (let i = 0; i < 8; i++) {
            const date = new Date(today);
            date.setDate(today.getDate() + i);
            dates.push(date.toISOString().split("T")[0]);
        }
        return dates;
    };

    const renderDates = () => {
        const dates = generateDates();
        datesContainer.innerHTML = "";
        dates.forEach(date => {
            const li = document.createElement("li");
            li.textContent = date;
            li.addEventListener("click", () => loadMatches(date));
            datesContainer.appendChild(li);
        });
    };

    const loadMatches = async (date) => {
        const response = await fetch(`/api/matches?date=${date}`);
        const matches = await response.json();
        renderMatches(matches);
    };

    const renderMatches = (matches) => {
        matchesTable.innerHTML = "";
        matches.forEach(match => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${match.fixture.date}</td>
                <td>${match.league.name}</td>
                <td>${match.teams.home.name}</td>
                <td>${match.teams.away.name}</td>
                <td>${match.fixture.status.short}</td>
            `;
            matchesTable.appendChild(row);
        });
    };

    renderDates();
    loadMatches(generateDates()[0]);
});
