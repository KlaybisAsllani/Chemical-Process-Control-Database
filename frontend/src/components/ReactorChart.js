import React, { useRef, useEffect } from 'react';
import * as d3 from 'd3';

const ReactorChart = ({ data }) => {
    const svgRef = useRef();

    useEffect(() => {
        const svg = d3.select(svgRef.current)
            .attr("width", 500)
            .attr("height", 300)
            .style("background", "#f0f0f0")
            .style("margin-top", "50")
            .style("overflow", "visible");

        const xScale = d3.scaleBand()
            .domain(data.map((val) => val.name))
            .range([0, 480])
            .padding(0.4);

        const yScale = d3.scaleLinear()
            .domain([0, 100])
            .range([300, 0]);

        const xAxis = d3.axisBottom(xScale);
        const yAxis = d3.axisLeft(yScale);

        svg.append("g")
            .call(xAxis)
            .attr("transform", "translate(10, 300)");

        svg.append("g")
            .call(yAxis)
            .attr("transform", "translate(10, 0)");

        svg.selectAll(".bar")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", (d) => xScale(d.name) + 10)
            .attr("y", (d) => yScale(d.conversion))
            .attr("width", xScale.bandwidth())
            .attr("height", (d) => 300 - yScale(d.conversion))
            .attr("fill", "orange");
    }, [data]);

    return (
        <div>
            <svg ref={svgRef}></svg>
        </div>
    );
}

export default ReactorChart;