// $('.curr-form').submit(function (evt) {
//     evt.preventDefault();

// })

// class NewLookUp {

//     constructor() {
//         this.words = new Set();
//     }



//     async handleSubmit(evt) {
//         evt.preventdefault();
//     }
// }


// async handleSubmit(evt) {
//     evt.preventDefault();
//     const $word = $(".word", this.board);

//     let word = $word.val();
//     if (!word) return;

//     if (this.words.has(word)) {
//         this.showMessage(`Already found ${word}`, "err");
//         return;
//     }

//     // check server for validity
//     const resp = await axios.get("/check-word", { params: { word: word } });
//     if (resp.data.result === "not-word") {
//         this.showMessage(`${word} is not a valid English word`, "err");
//     } else if (resp.data.result === "not-on-board") {
//         this.showMessage(`${word} is not a valid word on this board`, "err");
//     } else {
//         this.showWord(word);
//         this.score += word.length;
//         this.showScore();
//         this.words.add(word);
//         this.showMessage(`Added: ${word}`, "ok");
//     }

//     $word.val("").focus();
// }
