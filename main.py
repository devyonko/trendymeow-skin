import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure
fig, ax = plt.subplots(figsize=(6, 8))

# --- Measurements (mm) ---
d_big = 19
r_big = d_big / 2
d_small = 8
r_small = d_small / 2

# Gaps
gap_left_vert = 2.5   # Between two big lenses
gap_right_vert = 11   # Between depth sensor and flash
gap_horiz = 6         # Between Left Lens edge and Right Sensor edge

# --- Coordinates ---
# 1. Establish Left Column (Big Lenses) centered at X=0
# Top Left Center
y_cl_top = (gap_left_vert / 2) + r_big
# Bottom Left Center
y_cl_bot = -((gap_left_vert / 2) + r_big)
x_cl = 0

# 2. Establish Right Column (Small Sensors)
# X Position: Radius Big + Gap + Radius Small
x_cr = r_big + gap_horiz + r_small
# Top Right Center
y_cr_top = (gap_right_vert / 2) + r_small
# Bottom Right Center
y_cr_bot = -((gap_right_vert / 2) + r_small)

# 3. Calculate Island (Bounding Box) Size
# Width = Big Dia (19) + Gap (6) + Small Dia (8) + Side Padding (approx 1.5mm * 2)
# Let's set Island Width to 36mm to satisfy >3.5cm constraint
island_width = 36
island_height = 45 # A bit taller than the 40.5mm component height

# Center of Island (approximate shift to enclose all)
# The left edge of big lens is at x = -9.5. Right edge of small is at x = 19.5 + 4 = 23.5.
# Total span = 33mm. Center X = (-9.5 + 23.5)/2 = 7.
island_center_x = 7
island_center_y = 0

# --- Draw ---
# 1. Draw Island (The raised bump)
island_rect = patches.FancyBboxPatch(
    (island_center_x - island_width/2, island_center_y - island_height/2),
    island_width, island_height,
    boxstyle=f"round,pad=0,rounding_size=4",
    linewidth=2, edgecolor='#555555', facecolor='#f0f0f0', label='Camera Island (>3.5cm)'
)
ax.add_patch(island_rect)

# 2. Draw Sensors
c1 = patches.Circle((x_cl, y_cl_top), r_big, edgecolor='blue', facecolor='#aaccee', lw=2, label='Big Lens (1.9cm)')
c2 = patches.Circle((x_cl, y_cl_bot), r_big, edgecolor='blue', facecolor='#aaccee', lw=2)
c3 = patches.Circle((x_cr, y_cr_top), r_small, edgecolor='red', facecolor='#ffccaa', lw=2, label='Sensor/Flash (0.8cm)')
c4 = patches.Circle((x_cr, y_cr_bot), r_small, edgecolor='red', facecolor='#ffccaa', lw=2)

ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c4)

# --- Dimensions & Annotations ---
# Island Dimensions
ax.text(island_center_x, island_center_y + island_height/2 + 2, f"Island Width: {island_width}mm", ha='center', fontsize=10, fontweight='bold')
ax.text(island_center_x, island_center_y - island_height/2 - 4, f"Island Height: {island_height}mm", ha='center', fontsize=10)

# Component Gaps
ax.annotate(f"{gap_horiz}mm Gap", xy=(x_cl+r_big, y_cl_top), xytext=(x_cl+r_big+gap_horiz/2, y_cl_top), 
            arrowprops=dict(arrowstyle='<->', color='purple'), color='purple', ha='center', va='bottom', rotation=90)

# Left Vertical Gap
ax.annotate(f"{gap_left_vert}mm", xy=(x_cl, y_cl_top-r_big), xytext=(x_cl-12, 0),
            arrowprops=dict(arrowstyle='-', color='green'), color='green', va='center')

# Right Vertical Gap
ax.annotate(f"{gap_right_vert}mm", xy=(x_cr, y_cr_top-r_small), xytext=(x_cr+10, 0),
            arrowprops=dict(arrowstyle='-', color='green'), color='green', va='center')

# Settings
ax.set_xlim(-20, 40)
ax.set_ylim(-30, 35)
ax.set_aspect('equal')
plt.title(f"Oppo K13 Camera Module Blueprint", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()