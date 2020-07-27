async function draw_all_charts() {
    let blog_graphs = document.getElementsByClassName("blog_graph");
    for (blog_graph of blog_graphs) {
        // dataset gives acces to data-chart-date_from="{{ post.date_from }}" from template
        let chart_type = blog_graph.dataset.chart_type;
        let date_from = blog_graph.dataset.chart_date_from;
        let api_url = `http://127.0.0.1:8000/api/posts/?date_from=${date_from}`;        
        let chart_data_json = await fetch(api_url);
        if (chart_data_json.ok) { // if HTTP-status is 200-299
            // get the response body (the method explained below)
            let data_json = await chart_data_json.json();
            let chart_area = blog_graph.querySelector(".chart");
            let title_len_array = data_json.map((p) => {return p.title.length});
            let text_len_array = data_json.map((p) => {return p.text.length});
            let n_array1 = ['title_len'];
            let n_array2 = ['text_len'];
            n_array1.push(...title_len_array);
            n_array2.push(...text_len_array);
            let chart = c3.generate({
                bindto: chart_area,
                data: {
                  columns: [n_array1, n_array2]
                }
            });
            let graph_status = blog_graph.querySelector('#chart_status');
            graph_status.innerHTML = "Ready!";
        } else {
            alert("HTTP-Error: " + chart_data_json.status);
        };
        

    };
};