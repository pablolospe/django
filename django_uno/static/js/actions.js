let endpoint = "https://api.binance.com/api/v3/ticker/price"

fetch(endpoint)
.then(response => response.json())
.then(data => mostrarData(data))
.catch(e=> console.log(e))

const diccionario = [
    {
        symbol: 'BTCUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'
    },
    {
        symbol: 'ETHUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'
    },
    {
        symbol: 'BNBUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'
    },
    {
        symbol: 'XRPUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'
    },
    {
        symbol: 'SOLUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png'
    },
    {
        symbol: 'ADAUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'
    },
    {
        symbol: 'DOGEUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'
    },
    {
        symbol: 'TRXUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1958.png'
    },
    {
        symbol: 'GASUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1785.png'
    },
    {
        symbol: 'MATICUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png'
    },
    {
        symbol: 'DOTUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'
    },
    {
        symbol: 'LTCUSDT',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/2.png'
    },
]

const mostrarData= (data)=>{
    // console.log(data);

    let filtro = data.filter(d => diccionario.some(entry => entry.symbol === d.symbol));

    console.log(filtro);

    let symbol = ''
    for (let i = 0; i < filtro.length; i++) {

        const img = diccionario.find(entry => entry.symbol === filtro[i].symbol).img;

        symbol =`<div id="ETHUSDT" class="price-container">
        <img class="coin-logo" src=${img} alt="coin-logo"/>
        <div class="row"><h3 >${filtro[i].symbol}</h3><p>Price:</p> <p> ${parseFloat(filtro[i].price).toFixed(2)}</p></div></div>`

        document.getElementById('main').innerHTML += symbol
    }


}
