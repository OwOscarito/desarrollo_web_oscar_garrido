function pageSwitcher(currentPage, pageCount, maxDelta = 5) {
  const elem = document.createElement('div');
  elem.id = 'page-switcher';

  const startPage = Math.max(1, currentPage - maxDelta);
  const endPage = Math.min(pageCount, currentPage + maxDelta);

  if (startPage > 1) {
    const firstPageLink = document.createElement('a');
    firstPageLink.className = 'button';
    firstPageLink.href = `/listado/1`;
    firstPageLink.textContent = '1';
    elem.appendChild(firstPageLink);

    if (startPage > 2) {
      const ellipsis = document.createElement('span');
      ellipsis.className = 'ellipsis';
      ellipsis.textContent = '...';
      elem.appendChild(ellipsis);
    }
  }
  for (let i = startPage; i <= endPage; i++) {
    let pageLink = document.createElement('a');
    if (i === currentPage) {
      pageLink = document.createElement('button');
      pageLink.href = '#';
      pageLink.disabled = true;
    } else {
      pageLink.className = 'button';
      pageLink.href = `/listado/${i}`;
    }
    pageLink.textContent = i;
    elem.appendChild(pageLink);
  }
  if (endPage < pageCount) {
      if (endPage < pageCount - 1) {
        const ellipsis = document.createElement('span');
        ellipsis.className = 'ellipsis';
        ellipsis.textContent = '...';
        elem.appendChild(ellipsis);
      }
      const lastPageLink = document.createElement('a');
      lastPageLink.className = 'button';
      lastPageLink.href = `/listado/${pageCount}`;
      lastPageLink.textContent = pageCount;
      elem.appendChild(lastPageLink);
  }
  return elem;
}
window.onload = () => {
  let MAX_PAGE = 5;
  const container = document.getElementById("page-switcher-container");
  container.appendChild(pageSwitcher(pageNum, MAX_PAGE));
}