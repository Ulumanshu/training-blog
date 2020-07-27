function find_all_chart_elements() {
    let blog_graphs = document.getElementsByClassName("blog_graph");
    for (blog_graph of blog_graphs) {
        console.log('IWORK TOO', blog_graph)
        let chart_type = blog_graph.dataset.chart_type
        let date_from = blog_graph.dataset.date_from
        let chart_area = blog_graph.querySelector(".chart");
        let chart = c3.generate({
            bindto: chart_area,
            data: {
              columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 50, 20, 10, 40, 15, 25]
              ]
            }
        });

      }
}