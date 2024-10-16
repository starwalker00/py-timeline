import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from datetime import datetime

current_year = datetime.now().year

# Sample data for musicians, their eras, and lifespans
musicians = [
    ("Palestrina", 1525, 1594, "Renaissance"),
    ("Monteverdi", 1567, 1643, "Renaissance"),
    ("Bach", 1685, 1750, "Baroque"),
    ("Handel", 1685, 1759, "Baroque"),
    ("Vivaldi", 1678, 1741, "Baroque"),
    ("Rameau", 1683, 1764, "Baroque"),
    ("Domenico Scarlatti", 1685, 1757, "Baroque"),
    ("Telemann", 1681, 1767, "Baroque"),
    ("Haydn", 1732, 1809, "Classical"),
    ("Gluck", 1714, 1787, "Classical"),
    ("Salieri", 1750, 1825, "Classical"),
    ("Mozart", 1756, 1791, "Classical"),
    ("Beethoven", 1770, 1827, "Classical"),
    ("Clementi", 1752, 1832, "Classical"),
    ("Schubert", 1797, 1828, "Romantic"),
    ("Rossini", 1792, 1868, "Romantic"),
    ("Mendelssohn", 1809, 1847, "Romantic"),
    ("Chopin", 1810, 1849, "Romantic"),
    ("Schumann", 1810, 1856, "Romantic"),
    ("Liszt", 1811, 1886, "Romantic"),
    ("Wagner", 1813, 1883, "Romantic"),
    ("Verdi", 1813, 1901, "Romantic"),
    ("Tchaikovsky", 1840, 1893, "Romantic"),
    ("Brahms", 1833, 1897, "Romantic"),
    ("Saint-Saëns", 1835, 1921, "Romantic"),
    ("Mahler", 1860, 1911, "Romantic"),
    ("Debussy", 1862, 1918, "Modern"),
    ("Sibelius", 1865, 1957, "Modern"),
    ("Puccini", 1858, 1924, "Modern"),
    ("Ravel", 1875, 1937, "Modern"),
    ("Stravinsky", 1882, 1971, "Modern"),
    ("Schoenberg", 1874, 1951, "Modern"),
    ("Shostakovich", 1906, 1975, "Modern"),
    ("Bartók", 1881, 1945, "Modern"),
    ("Prokofiev", 1891, 1953, "Modern"),
    ("John Cage", 1912, 1992, "Contemporary"),
    ("Philip Glass", 1937, current_year, "Contemporary"),
    ("Arvo Pärt", 1935, current_year, "Contemporary"),
]

# British Monarchs data
monarchs = [
    ("Elizabeth I", 1533, 1603),
    ("James I", 1603, 1625),
    ("Charles I", 1625, 1649),
    ("Victoria", 1837, 1901),
    ("George VI", 1936, 1952),
    ("Elizabeth II", 1952, 2022),
]

french_monarchs = [
    ("François I", 1515, 1547),  # First significant Renaissance monarch in France
    # ("Henry II", 1547, 1559),
    # ("Francis II", 1559, 1560),
    # ("Charles IX", 1560, 1574),
    # ("Henry III", 1574, 1589),
    # ("Henry IV", 1589, 1610),  # First Bourbon king
    # ("Louis XIII", 1610, 1643),
    ("Louis XIV", 1643, 1715),  # Longest reigning French monarch, the Sun King
    ("Louis XV", 1715, 1774),
    ("Louis XVI", 1774, 1792),  # Executed during the French Revolution
    ("Napoleon I", 1804, 1815),  # Emperor of the French
    # ("Louis XVIII", 1815, 1824),  # Bourbon Restoration
    # ("Charles X", 1824, 1830),
    # ("Louis-Philippe I", 1830, 1848),  # Last King of France
    ("Napoleon III", 1852, 1870)  # Emperor of the French, Second Empire
]

# Periods (start, end, name)
periods = [
    (1500, 1600, "Renaissance"),
    (1600, 1750, "Baroque"),
    (1750, 1820, "Classical"),
    (1820, 1900, "Romantic"),
    (1900, 1975, "Modern"),
    (1975, 2050, "Contemporary"),
]

# Assign colors to different eras
era_colors = {
    "Renaissance": "blue",
    "Baroque": "green",
    "Classical": "orange",
    "Romantic": "red",
    "Modern": "purple",
    "Contemporary": "blue",
}

# Plot the timeline
fig, ax = plt.subplots(figsize=(12, 8))


# Function to draw custom composer or monarch labels
def draw_label(name, start, end, y_pos, color="black"):
    # Draw the horizontal line for lifespan
    ax.plot([start, end], [y_pos, y_pos], color=color, lw=2)

    # Draw circles at both ends
    ax.plot(start, y_pos, "o", color=color)
    ax.plot(end, y_pos, "o", color=color)

    # Add the musician's name inside the box
    ax.text((start + end) / 2, y_pos, name, ha="center", va="center", fontsize="small",
        bbox=dict(
            pad=0.1,
            boxstyle="round",
            facecolor="lightgray",
            edgecolor='none',
        ),
    )


# Plot musicians with custom labels
musician_y_pos = 1
for i, (musician, start, end, era) in enumerate(musicians):
    draw_label(musician, start, end, musician_y_pos, era_colors[era])
    # if i > 0:
    #     ax.axhline(y=i + 0.5, color='gray', linestyle='--', linewidth=0.5)  # Horizontal separator
    musician_y_pos += 1  # Stagger vertically to avoid overlap


# Plot British Monarchs on a separate row below composers
monarch_y_pos = -1
for i, (monarch, start, end) in enumerate(monarchs):
    draw_label(monarch, start, end, monarch_y_pos, color="brown")
    monarch_y_pos -= 1  # Stagger vertically to avoid overlap

# Separate British and French monarchs
ax.axhline(y=monarch_y_pos + 0.5, linewidth=1, color="red")

# Plot French Monarchs
for i, (monarch, start, end) in enumerate(french_monarchs):
    draw_label(monarch, start, end, monarch_y_pos, color="brown")
    monarch_y_pos -= 1  # Stagger vertically to avoid overlap

# Separate musicians and monarchs
ax.axhline(y=0, linewidth=2, color="r")

# Adding periods (like Renaissance, Baroque etc.)
for start, end, name in periods:
    # ax.axvline(x=start, linewidth=1, color='r')
    # ax.axvline(x=end, linewidth=1, color='r')
    ax.fill_betweenx(
        [monarch_y_pos - 1, musician_y_pos + 1],
        start,
        end,
        color=era_colors[name],
        alpha=0.1,
    )  # Shaded region for each period
    ax.text((start + end) / 2, musician_y_pos, name, ha="center", fontsize=12, fontweight="bold",
        bbox=dict(
            boxstyle="round",
            facecolor='snow',
            edgecolor='none',
        ),
    )  # Period label on top

# Customizing the plot
ax.set_yticks([])  # Remove y-ticks
ax.set_title("Music History Timeline with British Monarchs")

# major
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.grid(visible=True, which="major", linestyle="-", linewidth=1, color="black", alpha=0.8)
ax.tick_params(axis="x", which="major", labelsize="large")
# minor
ax.xaxis.set_minor_locator(MultipleLocator(25))
ax.xaxis.grid(visible=True, which="minor", linestyle="--", linewidth=0.5, color="black", alpha=0.4)
ax.xaxis.set_minor_formatter(lambda x, pos: str(int(x))[-2:])  # Display 25 instead of 1625
ax.tick_params(axis="x", which="minor", labelsize="small")

# Limiting the x and y axis to fit the content
ax.set_xlim(1500, 2050)
ax.set_ylim(monarch_y_pos - 1, musician_y_pos + 1)

# Show the plot
plt.tight_layout()
plt.show()


plt.savefig("timeline1.svg", format="svg")
