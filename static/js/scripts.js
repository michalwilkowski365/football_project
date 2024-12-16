document.addEventListener("DOMContentLoaded", () => {
    const countriesList = document.getElementById("countries");
    const matchesTable = document.getElementById("matches").querySelector("tbody");

    let selectedLeagues = new Set();

    const fetchLeagues = async () => {
        const response = await fetch("/api/leagues");
        const data = await response.json();

        const sortedCountries = Object.keys(data).sort(); // Sortowanie alfabetyczne krajów

        sortedCountries.forEach(country => {
            const countryItem = document.createElement("li");
            countryItem.textContent = country;

            const leagueList = document.createElement("ul");

            Object.entries(data[country]).forEach(([leagueName, leagueId]) => {
                const leagueItem = document.createElement("li");

                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.dataset.leagueId = leagueId;

                // Kliknięcie w nazwę ligi lub checkbox obsługuje zaznaczanie
                leagueItem.addEventListener("click", (event) => {
                    event.stopPropagation(); // Zapobiega zamykaniu rozwiniętej listy
                    checkbox.checked = !checkbox.checked;
                    if (checkbox.checked) {
                        selectedLeagues.add(leagueId);
                    } else {
                        selectedLeagues.delete(leagueId);
                    }
                    loadMatches();
                });

                leagueItem.appendChild(checkbox);
                leagueItem.appendChild(document.createTextNode(leagueName));
                leagueList.appendChild(leagueItem);
            });

            countryItem.appendChild(leagueList);
            countryItem.addEventListener("click", () => {
                const isHidden = leagueList.style.display === "none";
                leagueList.style.display = isHidden ? "block" : "none";
            });

            countriesList.appendChild(countryItem);
        });
    };

    const loadMatches = async () => {
        const today = new Date().toISOString().split("T")[0];
        const selectedLeagueIds = Array.from(selectedLeagues).join(",");
        
        if (selectedLeagueIds) {
            const response = await fetch(`/api/matches?league=${selectedLeagueIds}&date=${today}&season=2024`);
            const matches = await response.json();
            
            renderMatches(matches);
        } else {
            matchesTable.innerHTML = ""; // Pusta tabela, gdy nic nie zaznaczono
        }
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

    fetchLeagues();
});
