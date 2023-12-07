let endpoint = "https://api.binance.com/api/v3/ticker/price"

fetch(endpoint)
.then(response => response.json())
.then(data => mostrarData(data))
.catch(e=> console.log(e))

const diccionario = [
    {
        symbol: 'BTCUSDT',
        link: 'https://bitcoin.org/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'
    },
    {
        symbol: 'ETHUSDT',
        link: 'https://ethereum.org/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'
    },
    {
        symbol: 'BNBUSDT',
        link: 'https://www.bnbchain.org/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'
    },
    {
        symbol: 'XRPUSDT',
        link: 'https://xrpl.org/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'
    },
    {
        symbol: 'SOLUSDT',
        link: 'https://solana.com/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png'
    },
    {
        symbol: 'ADAUSDT',
        link: 'https://cardano.org/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'
    },
    {
        symbol: 'DOGEUSDT',
        link: 'https://dogecoin.com/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'
    },
    {
        symbol: 'TRXUSDT',
        link: 'https://tron.network/usdt',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1958.png'
    },
    {
        symbol: 'GASUSDT',
        link: 'https://es.tradingview.com/symbols/GASUSD/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/1785.png'
    },
    {
        symbol: 'MATICUSDT',
        link: 'https://polygon.technology/',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png'
    },
    {
        symbol: 'DOTUSDT',
        link: 'https://www.binance.com/en/trade/DOT_USDT?type=spot',
        img: 'https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'
    },
    {
        symbol: 'LTCUSDT',
        link: 'https://litecoin.com/',
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
        const link = diccionario.find(entry => entry.symbol === filtro[i].symbol).link;

        symbol =`<a href=${link} target="_blank">
        <div>
        <div  class="price-container">
        <img class="coin-logo" src=${img} alt="coin-logo"/>
        <div class="row">
        <h3>${filtro[i].symbol}</h3><p>Price:</p> <p> ${parseFloat(filtro[i].price).toFixed(2)}</p></div></div>
        </div>
        </a>`

        document.getElementById('main').innerHTML += symbol
    }


}
