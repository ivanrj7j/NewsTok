const getNextPost = async () =>{
    const response = await fetch("/getNext");
    return await response.json();
};

let currentPost;

const updatePage = async () =>{
    const postData = await getNextPost();
    currentPost = postData.url;

    let contentDIV = document.querySelector(".content");

    const titleTag = document.querySelector(".title");
    const authorTag = document.querySelector(".author");
    const summaryTag = document.querySelector(".summary");

    titleTag.innerHTML = `<h1>${postData.title}<h2>`;
    authorTag.innerHTML = `<h5>${postData.author}<h5>`;
    summaryTag.innerHTML = `<p>${postData.summary}<p>`;

    [titleTag, authorTag, summaryTag].forEach((tag)=>{
        tag.href = postData.url;
    });
    
    contentDIV.style.backgroundImage = `url(${postData.cover})`;
};

document.addEventListener("DOMContentLoaded", updatePage);