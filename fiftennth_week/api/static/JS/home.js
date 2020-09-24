/* 
첫 번째로 api에서 받은 key, default 날짜로 구성된 url을 임의로 설정하고 
해당 일자의 rank 데이터를 받아 html에 전송해주는 기초적인 과정을 다뤄볼게요
< Contents >
1. key 받아와 날짜정보를 임의로 작성해서 url로 보내주기
2. async & await & promise object 맛보기
3. rank 데이터 받아서 html에 쏴주기 
*/
let lastDay = new Date((new Date()) - 1000*60*60*24).toISOString().substring(0,10);
let dateInput = document.querySelector(".todayDateInput");
dateInput.value = lastDay;
dateInput.setAttribute("max", lastDay);
let contentsBox = document.querySelector('.contents'); // 그냥 html에 있는 class contents div
const key = "?key=a16a9af0a191b5cd7468720d54f2ab95"; // api key를 가져왔습니다.
let movieCodeObject = {};
let movieNameArray = [];
let movieCodeArray = [];


const clickedSearchBtn = async() => {
    await giveRankObject() // await는 다음의 함수가 실행을 모두 마칠 때까지 잠시만 기다려주겠다는 뜻이에요
    .then((data) => { // 위의 함수에서 반환된 값을 data라는 이름을 붙여 사용하겠다는 뜻이에요
        let DtYear = data.boxOfficeResult.showRange.substring(0,4);
        let DtMonth = data.boxOfficeResult.showRange.substring(4,6);
        let DtDate = data.boxOfficeResult.showRange.substring(6,8);
        // substring을 이용해서 20200906~20200906 형태에서 원하는 부분만 잘랐어요 
        // 더 간략하게 할 수 있을거 같은데 일단 이렇게!
        let dateTitle = document.createTextNode(`${DtYear}년 ${DtMonth}월 ${DtDate}일 박스 오피스`);
        //appenchild해주기 위해 textnode로 담아 주시고
        let titleBox = document.createElement('h1');
        // h1 태그도 하나 만들어주시고
        let createDiv = document.createElement('div');
        //div도 만들어주시고
        createDiv.classList.add("moviePackage");
        // 만든 div 클래스에 moviePackage 를 추가해 주시고
        contentsBox.appendChild(createDiv).appendChild(titleBox).appendChild(dateTitle);
        // contentsBox 속에 만든 div 그 속에 titleBox(h1 태그) h1태그 글자를 dateTitle로 해줍시다.
        for (let i = 0; i < 10; i++) {
            let movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm;
            let movieCodeJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieCd;
            let text = document.createTextNode(`${i+1}위 `+movieRankJson);
            //~~위 를 표시하기 위해 `${i+1}위 `를 추가했어요
            let textBox = document.createElement('button');
            // p태그 만들어주시고
            contentsBox.appendChild(createDiv).appendChild(textBox).appendChild(text);
            // contentsBox 속에 만든 div 그 속에 textBox(p 태그) p태그 글자를 text(~위 영화제목)로 해줍시다.
            textBox.setAttribute("value", `${movieRankJson}`); // setAttribute는 해당 태그에 속성값을 부여할 수 있다.\
            textBox.setAttribute("onclick", "ClickedMovieBtn(this);");

            movieNameArray[i] = `${movieRankJson}`;
            movieCodeArray[i] = `${movieCodeJson}`;
            movieCodeObject[movieNameArray[i]] = `${movieCodeArray[i]}` //object를 만드는 방법으로 movieNameArray[i] : "movieCodeArray[i]" 이런식으로 담긴다. (키 : 벨류 요런식으로)
        };
    })
    .catch(error => console.log(`에러 발생 ${error.name}:${error.message}`));
};


/* async function은 promise object를 return 합니다 
search 함수를 불러오면 return promise object가 완료될때 까지 기다려줄거에요*/
const giveRankObject = async() => {
    let date = document.todayDateForm.todayDateInput.value;
    let targetDate = date.replaceAll("-", "");
    let targetTodayDate = `&targetDt=${targetDate}`; // 검색형식이에요
    const url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    + key
    + targetTodayDate; // 검색할 json파일 url 입니다
    const response = await fetch(url);
    return await response.json(); // text, arrayBuffer, blob, json, formData 종류가 있어요
}
/* 기다림이 끝나고 promise object를 data라는 (임의)이름으로 사용할거에요
.then()을 통해서 promise object 가공합니다.*/

const showMeTheCode = async(clickedValue) => { // clickedValue에는 영화의 p테그 전체가 담겨옴
    let iWantedValue = clickedValue.value; // p테그 안에 value에 접근
    /* let Code = movieCodeObjectp[iWantedValue]; // object의 key를 []안에 넣어줘서 value를 가져오기. 그런데, 이럴 경우 object의 숫자가 많아지면, await를 이용(동기적으로)해야할 수 있음 그래서 함수로 지정하여 받아 올 것임 */
    let Code = CodeInMovieObj(iWantedValue); // 영화이름을 CodeInMovieObj 보내쥼
    let moreInfo = await searchMoreInfo(Code);
    return await moreInfo;
}

const CodeInMovieObj = async(clickedValue) => { // 영화이름을 받고
    let iWantedCode = movieCodeObject[clickedValue] // 오브젝트에서 영화이름으로 코드를 찾음
    return await iWantedCode; // 코드를 넘겨줌
}

const searchMoreInfo = async(Code) => {
    let usingCode = `&movieCd=${Code}`; // &꼴인 이유는 API 검색을 위한 형식에 맞추기 위해서 사용함
    const infoUrl = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    + key
    + usingCode; // 검색할 json파일 url 입니다
    const responseInfo = await fetch(infoUrl);
    return await responseInfo.json();
}

const ClickedMovieBtn = async(clickedValue) => {
    console.log(clickedValue);
    await showMeTheCode(clickedValue);
        .then((info) => {
            console.log(info);
        })
};

    // 이전 방법 동작하지않을수도..?

/* fetch(url, {
    method="GET",
    headers={
        'Content-Type': 'application/json',
        '필요하다면' : '이렇게 보내요'
      }
})
    .then(response => response.json()) 
    .then((data) => {
        for (let i = 0; i < 10; i++) {
            movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm; 
            let text = document.createTextNode(movieRankJson);
            contentsBox.appendChild(text);
        }
    })
    .catch(error => console.log(`에러 발생 ${error.name}:${error.message}`));
 */