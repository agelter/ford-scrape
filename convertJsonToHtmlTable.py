import json
from pathlib import Path

# Create an HTML table
html_table = """<script src="https://www.w3.org/WAI/content-assets/wai-aria-practices/patterns/table/examples/js/sortable-table.js"></script>
<link rel="stylesheet" type="text/css" href="https://www.w3.org/WAI/content-assets/wai-aria-practices/patterns/table/examples/css/sortable-table.css">

<div class="table-wrap"><table class="sortable">
    <caption>
      Students currently enrolled in WAI-ARIA 101
      <span class="sr-only">, column headers with buttons are sortable.</span>
    </caption>
    <thead>
      <tr>
        <th>
          <button>
            Dealer
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th aria-sort="ascending">
          <button>
            Title
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            DriveLine
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            Engine
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            Trim
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            MSRP
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            VIN
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            ExteriorColor
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th>
          <button>
            InteriorColor
            <span aria-hidden="true"></span>
          </button>
        </th>
        <th class="no-sort">Link</th>
      </tr>
    </thead>
    <tbody>
"""

json_data = json.loads(Path('./combined_results.json').read_text())

for entry in json_data:
    if 'hybrid' in entry['engine'].lower():
        html_table += "<tr>"
        html_table += "<td>{}</td>".format(entry["dealer"])
        html_table += "<td>{}</td>".format(entry["title"])
        html_table += "<td>{}</td>".format(entry["driveLine"])
        html_table += "<td>{}</td>".format(entry["engine"])
        html_table += "<td>{}</td>".format(entry["trim"])
        html_table += "<td>{}</td>".format(entry["msrp"])
        html_table += "<td>{}</td>".format(entry["vin"])
        html_table += "<td>{}</td>".format(entry["exteriorColor"])
        html_table += "<td>{}</td>".format(entry["interiorColor"])
        html_table += "<td><a href='{}'>Link</a></td>".format(entry["link"])
        html_table += "</tr>\n"

html_table += """</tbody>
</table></div>
"""

# Save the HTML table with DataTables JavaScript to a file
with open("current_listings.html", "w") as file:
    file.write(html_table)

print("Sortable HTML table with DataTables saved to 'sortable_table.html'")

