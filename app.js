const API_URL = "http://127.0.0.1:8000";

// 1. Fonction pour charger et afficher la liste des biens
async function chargerBiens() {
    try {
        const response = await fetch(`${API_URL}/biens/`);
        const biens = await response.json();
        
        const tableBody = document.getElementById('biensTableBody');
        tableBody.innerHTML = ''; // On vide le tableau avant de le remplir

        biens.forEach(bien => {
            const row = `
                <tr>
                    <td>${bien.id}</td>
                    <td><strong>${bien.code_ref}</strong></td>
                    <td>${bien.type_bien}</td>
                    <td>${bien.loyer_hc}</td>
                    <td>${bien.charges}</td>
                    <td>${bien.statut}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });
    } catch (error) {
        console.error("Erreur lors du chargement des biens:", error);
    }
}

// 2. Écouteur d'événement pour soumettre le formulaire
document.getElementById('bienForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Empêche la page de se recharger

    const nouveauBien = {
        code_ref: document.getElementById('code_ref').value,
        type_bien: document.getElementById('type_bien').value,
        loyer_hc: parseFloat(document.getElementById('loyer_hc').value),
        charges: parseFloat(document.getElementById('charges').value)
    };

    try {
        const response = await fetch(`${API_URL}/biens/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nouveauBien)
        });

        if (response.ok) {
            document.getElementById('bienForm').reset(); // Vide le formulaire
            chargerBiens(); // Rafraîchit le tableau automatiquement
        } else {
            alert("Erreur lors de l'ajout (Vérifiez si la référence existe déjà)");
        }
    } catch (error) {
        console.error("Erreur:", error);
    }
});

// 3. Charger les biens au démarrage de la page
chargerBiens();


// 1. Fonction pour charger et afficher la liste des locataires
async function chargerLocataires() {
    try {
        const response = await fetch(`${API_URL}/locataires/`);
        const locataires = await response.json();
        
        const tableBody = document.getElementById('locatairesTableBody');
        tableBody.innerHTML = ''; // On vide le tableau

        locataires.forEach(locataire => {
            const row = `
                <tr>
                    <td>${locataire.id}</td>
                    <td><strong>${locataire.nom}</strong></td>
                    <td>${locataire.prenom}</td>
                    <td>${locataire.telephone}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });
    } catch (error) {
        console.error("Erreur lors du chargement des locataires:", error);
    }
}

// 2. Écouteur d'événement pour soumettre le formulaire Locataire
document.getElementById('locataireForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const nouveauLocataire = {
        nom: document.getElementById('nom').value,
        prenom: document.getElementById('prenom').value,
        telephone: document.getElementById('telephone').value
    };

    try {
        const response = await fetch(`${API_URL}/locataires/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nouveauLocataire)
        });

        if (response.ok) {
            document.getElementById('locataireForm').reset();
            chargerLocataires(); // Rafraîchit le tableau
        } else {
            alert("Erreur lors de l'ajout du locataire.");
        }
    } catch (error) {
        console.error("Erreur:", error);
    }
});

// Appeler la fonction au démarrage pour afficher les locataires existants
chargerLocataires();