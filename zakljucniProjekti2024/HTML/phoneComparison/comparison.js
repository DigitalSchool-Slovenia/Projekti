function Phone(name, screen, camera, price, OS, CPU, GPU, memory, storage, imageURL) {
    this.name = name;
    this.screen = screen;
    this.camera = camera;
    this.price = price;
    this.OS = OS;
    this.CPU = CPU;
    this.GPU = GPU;
    this.memory = memory;
    this.storage = storage;
    this.imageURL = imageURL;
}

var phones = [
    new Phone("Samsung Galaxy S24 Ultra", "1440x3120px", "200MP, 12MP, 10MP, 50MP", "1.569,90 €", "Android 14", "Snapdragon 8 Gen 3", "Adreno 750", "12GB", "512GB", "./s24u.jpg"),
    new Phone("Nokia 3310", "320x240px", "non-existent", "59.99€", "AliOS", "MediaTek MT6260", "Doesn't have it", "18MB", "16MB", "./Nokia3310.jpg"),
    new Phone("motorola moto x50 ultra", "2712x1220px", "50mp, 64mp, 50mp", "550.10€", "Android 14", "Qualcomm snapdragon 8s Gen 3 ", "Qualcomm Andreno 735", "12gb", "512gb", "./motox50.jpg"),
    new Phone("Redmi Note 13 Pro+ 5G", "2712x1220px", "200MP, 8MP, 2MP", "546€", "Android 13", "MediaTek Dimensity 7200-Ultra", "Mali-G610 MC4", "12GB", "512GB", "./Redmi13pro.png")
];

var PhoneListDiv = document.getElementById("phones");
var phone1Select = document.getElementById('phone1');
var phone2Select = document.getElementById('phone2');

phones.forEach(function(phone, index) {
    // Create phone listing
    var phoneDiv = document.createElement("div");
    phoneDiv.classList.add("phone");
    phoneDiv.innerHTML = `
        <h2> ${phone.name}</h2>
        <p>Price: ${phone.price}</p>
        <p>Screen: ${phone.screen}</p>
        <p>OS: ${phone.OS}</p>
        <p>CPU: ${phone.CPU}</p>
        <p>GPU: ${phone.GPU}</p>
        <p>Memory: ${phone.memory}</p>
        <p>Storage: ${phone.storage}</p>`;
    
    var phoneImg = document.createElement("img");
    phoneImg.src = phone.imageURL;
    phoneImg.alt = phone.name;
    phoneDiv.appendChild(phoneImg);
    PhoneListDiv.appendChild(phoneDiv);
    
    // Add options to select elements
    var option1 = document.createElement("option");
    option1.value = index;
    option1.textContent = phone.name;
    phone1Select.appendChild(option1);
    
    var option2 = document.createElement("option");
    option2.value = index;
    option2.textContent = phone.name;
    phone2Select.appendChild(option2);
});

// Function to compare phones
document.getElementById("comparisonForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const phone1Index = document.getElementById('phone1').value;
    const phone2Index = document.getElementById('phone2').value;

    const phone1 = phones[phone1Index];
    const phone2 = phones[phone2Index];

    const comparisonResult = document.getElementById('comparisonResult');
    comparisonResult.innerHTML = `
        <h3>${phone1.name} vs ${phone2.name}</h3>
        <div>
            <img src="${phone1.imageURL}" alt="${phone1.name}">
            <ul>
                <li>Screen: ${phone1.screen}</li>
                <li>Camera: ${phone1.camera}</li>
                <li>Price: ${phone1.price}</li>
                <li>OS: ${phone1.OS}</li>
                <li>CPU: ${phone1.CPU}</li>
                <li>GPU: ${phone1.GPU}</li>
                <li>Memory: ${phone1.memory}</li>
                <li>Storage: ${phone1.storage}</li>
            </ul>
        </div>
        <div>
            <img src="${phone2.imageURL}" alt="${phone2.name}">
            <ul>
                <li>Screen: ${phone2.screen}</li>
                <li>Camera: ${phone2.camera}</li>
                <li>Price: ${phone2.price}</li>
                <li>OS: ${phone2.OS}</li>
                <li>CPU: ${phone2.CPU}</li>
                <li>GPU: ${phone2.GPU}</li>
                <li>Memory: ${phone2.memory}</li>
                <li>Storage: ${phone2.storage}</li>
            </ul>
        </div>
    `;
});
