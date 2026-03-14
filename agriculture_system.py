import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class Crop:
    CROP_INFO = {
        "Rice": {
            "planting_months": ["June", "July"],
            "water_needs": {"Planted": "High", "Growing": "High", "Harvesting": "Moderate"},
            "pests": ["Stem Borer", "Leafhopper"],
            "sell_months": ["November", "December"],
            "base_yield": 85,
            "growth_days": 90,
            "cost_breakdown": {"Seeds": 8000, "Fertilizers": 10000, "Labor": 10000, "Irrigation": 7000, "Pesticides": 5000},
            "total_cost": 40000,  # Per hectare in INR
            "msp": 2300,  # Per quintal in INR (2025 estimate)
            "rotation": ["Wheat", "Grams"]
        },
        "Wheat": {
            "planting_months": ["October", "November"],
            "water_needs": {"Planted": "Low", "Growing": "Moderate", "Harvesting": "Low"},
            "pests": ["Aphids", "Hessian Fly"],
            "sell_months": ["April", "May"],
            "base_yield": 80,
            "growth_days": 120,
            "cost_breakdown": {"Seeds": 6000, "Fertilizers": 8000, "Labor": 8000, "Irrigation": 5000, "Pesticides": 4000},
            "total_cost": 31000,
            "msp": 2500,
            "rotation": ["Grams", "Millets"]
        },
        "Millets": {
            "planting_months": ["July", "August"],
            "water_needs": {"Planted": "Low", "Growing": "Low", "Harvesting": "Low"},
            "pests": ["Shoot Fly", "Stem Borer"],
            "sell_months": ["December", "January"],
            "base_yield": 70,
            "growth_days": 80,
            "cost_breakdown": {"Seeds": 4000, "Fertilizers": 6000, "Labor": 7000, "Irrigation": 3000, "Pesticides": 3000},
            "total_cost": 23000,
            "msp": 3000,
            "rotation": ["Wheat", "Oilseeds"]
        },
        "Grams": {
            "planting_months": ["October", "November"],
            "water_needs": {"Planted": "Low", "Growing": "Moderate", "Harvesting": "Low"},
            "pests": ["Pod Borer", "Aphids"],
            "sell_months": ["February", "March"],
            "base_yield": 65,
            "growth_days": 90,
            "cost_breakdown": {"Seeds": 5000, "Fertilizers": 7000, "Labor": 8000, "Irrigation": 4000, "Pesticides": 4000},
            "total_cost": 28000,
            "msp": 6000,
            "rotation": ["Wheat", "Rice"]
        },
        "Sugarcane": {
            "planting_months": ["February", "March"],
            "water_needs": {"Planted": "High", "Growing": "High", "Harvesting": "Moderate"},
            "pests": ["Top Borer", "White Grub"],
            "sell_months": ["January", "February"],
            "base_yield": 90,
            "growth_days": 300,
            "cost_breakdown": {"Seeds": 20000, "Fertilizers": 15000, "Labor": 15000, "Irrigation": 10000, "Pesticides": 6000},
            "total_cost": 66000,
            "msp": 350,  # Per ton
            "rotation": ["Rice", "Cotton"]
        },
        "Cotton": {
            "planting_months": ["May", "June"],
            "water_needs": {"Planted": "Moderate", "Growing": "High", "Harvesting": "Low"},
            "pests": ["Bollworm", "Whitefly"],
            "sell_months": ["October", "November"],
            "base_yield": 75,
            "growth_days": 150,
            "cost_breakdown": {"Seeds": 10000, "Fertilizers": 10000, "Labor": 12000, "Irrigation": 8000, "Pesticides": 5000},
            "total_cost": 45000,
            "msp": 7000,
            "rotation": ["Wheat", "Soybean"]
        },
        "Oilseeds": {
            "planting_months": ["June", "July"],
            "water_needs": {"Planted": "Moderate", "Growing": "Moderate", "Harvesting": "Low"},
            "pests": ["Aphids", "Pod Borer"],
            "sell_months": ["November", "December"],
            "base_yield": 70,
            "growth_days": 120,
            "cost_breakdown": {"Seeds": 7000, "Fertilizers": 8000, "Labor": 9000, "Irrigation": 6000, "Pesticides": 4000},
            "total_cost": 34000,
            "msp": 5500,
            "rotation": ["Wheat", "Millets"]
        },
        "Tea": {
            "planting_months": ["March", "April"],
            "water_needs": {"Planted": "Moderate", "Growing": "Moderate", "Harvesting": "Moderate"},
            "pests": ["Tea Mosquito", "Red Spider Mite"],
            "sell_months": ["July", "August"],
            "base_yield": 60,
            "growth_days": 180,
            "cost_breakdown": {"Seeds": 30000, "Fertilizers": 10000, "Labor": 15000, "Irrigation": 7000, "Pesticides": 6000},
            "total_cost": 68000,
            "msp": 25000,  # Per ton
            "rotation": ["Coffee"]
        },
        "Coffee": {
            "planting_months": ["June", "July"],
            "water_needs": {"Planted": "Moderate", "Growing": "Moderate", "Harvesting": "Low"},
            "pests": ["Coffee Borer", "White Stem Borer"],
            "sell_months": ["December", "January"],
            "base_yield": 55,
            "growth_days": 200,
            "cost_breakdown": {"Seeds": 35000, "Fertilizers": 10000, "Labor": 15000, "Irrigation": 7000, "Pesticides": 6000},
            "total_cost": 73000,
            "msp": 100000,  # Per ton
            "rotation": ["Tea"]
        },
        "Corn": {
            "planting_months": ["April", "May"],
            "water_needs": {"Planted": "Moderate", "Growing": "High", "Harvesting": "Low"},
            "pests": ["Corn Borer", "Aphids"],
            "sell_months": ["September", "October"],
            "base_yield": 85,
            "growth_days": 100,
            "cost_breakdown": {"Seeds": 8000, "Fertilizers": 9000, "Labor": 10000, "Irrigation": 7000, "Pesticides": 5000},
            "total_cost": 39000,
            "msp": 2200,
            "rotation": ["Soybean", "Wheat"]
        },
        "Soybean": {
            "planting_months": ["May", "June"],
            "water_needs": {"Planted": "Moderate", "Growing": "Moderate", "Harvesting": "Low"},
            "pests": ["Soybean Aphid", "Spider Mites"],
            "sell_months": ["October", "November"],
            "base_yield": 75,
            "growth_days": 100,
            "cost_breakdown": {"Seeds": 7000, "Fertilizers": 8000, "Labor": 9000, "Irrigation": 6000, "Pesticides": 4000},
            "total_cost": 34000,
            "msp": 5000,
            "rotation": ["Corn", "Cotton"]
        },
        "Tomato": {
            "planting_months": ["March", "April"],
            "water_needs": {"Planted": "Moderate", "Growing": "High", "Harvesting": "Moderate"},
            "pests": ["Tomato Hornworm", "Whitefly"],
            "sell_months": ["July", "August"],
            "base_yield": 70,
            "growth_days": 90,
            "cost_breakdown": {"Seeds": 10000, "Fertilizers": 10000, "Labor": 12000, "Irrigation": 8000, "Pesticides": 5000},
            "total_cost": 45000,
            "msp": 2000,  # Per quintal
            "rotation": ["Corn", "Grams"]
        }
    }

    def __init__(self, name, planting_date, soil_quality, weather_condition, health_status, soil_type, land_area):
        if name not in self.CROP_INFO:
            raise ValueError(f"Unsupported crop: {name}")
        self.name = name
        self.planting_date = planting_date
        self.soil_quality = soil_quality
        self.weather_condition = weather_condition
        self.health_status = health_status
        self.soil_type = soil_type
        self.land_area = land_area  # In hectares
        self.growth_stage = "Planted"

    def update_growth_stage(self):
        days_since_planting = (datetime.now() - self.planting_date).days
        growth_days = self.CROP_INFO[self.name]["growth_days"]
        if days_since_planting < growth_days / 3:
            self.growth_stage = "Planted"
        elif days_since_planting < 2 * growth_days / 3:
            self.growth_stage = "Growing"
        else:
            self.growth_stage = "Harvesting"

    def get_info(self):
        return self.CROP_INFO[self.name]

class FarmManager:
    def __init__(self):
        self.crops = []

    def add_crop(self, crop):
        self.crops.append(crop)

    def get_crops(self):
        return self.crops

class Insights:
    @staticmethod
    def predict_yield(crop):
        info = crop.get_info()
        base_yield = info["base_yield"]
        soil_modifier = {"Good": 1.2, "Average": 1.0, "Poor": 0.8}.get(crop.soil_quality, 1.0)
        weather_modifier = {"Favorable": 1.3, "Moderate": 1.0, "Harsh": 0.7}.get(crop.weather_condition, 1.0)
        health_modifier = 0.9 if crop.health_status == "Stressed" else 1.0
        soil_type_modifier = {"Loamy": 1.1, "Clayey": 1.0, "Sandy": 0.9}.get(crop.soil_type, 1.0)
        yield_value = base_yield * soil_modifier * weather_modifier * health_modifier * soil_type_modifier
        return round(min(yield_value, 100), 2)

    @staticmethod
    def get_recommendations(crop):
        info = crop.get_info()
        crop.update_growth_stage()
        harvest_date = crop.planting_date + timedelta(days=info["growth_days"])
        total_cost = info["total_cost"] * crop.land_area
        cost_breakdown = "\n".join([f"{k}: ₹{v * crop.land_area:,}" for k, v in info["cost_breakdown"].items()])
        expected_yield = Insights.predict_yield(crop) / 100 * info["base_yield"] * crop.land_area * 10  # Quintals/ha
        profit = expected_yield * info["msp"] - total_cost
        rec = []
        rec.append(f"Water: {info['water_needs'][crop.growth_stage]}")
        rec.append(f"Fertilizer: {'Moderate' if crop.growth_stage == 'Growing' else 'Low'}")
        rec.append(f"Planting Time: {', '.join(info['planting_months'])}")
        rec.append(f"Pests to Watch: {', '.join(info['pests'])}")
        rec.append(f"Preventive Measures: Use organic pesticides, monitor regularly")
        rec.append(f"Best Sell Time: {', '.join(info['sell_months'])}")
        rec.append(f"Total Cost: ₹{total_cost:,}")
        rec.append(f"Cost Breakdown:\n{cost_breakdown}")
        rec.append(f"Expected Harvest: {harvest_date.strftime('%Y-%m-%d')}")
        rec.append(f"Next Crop: {info['rotation'][0]}")
        rec.append(f"Expected Yield: {expected_yield:.2f} quintals")
        rec.append(f"MSP: ₹{info['msp']:,}/{'ton' if crop.name in ['Sugarcane', 'Tea', 'Coffee'] else 'quintal'}")
        rec.append(f"Estimated Profit: ₹{profit:,.2f}")
        if crop.health_status == "Stressed":
            rec.append("Health Tip: Check for nutrient deficiency or water stress")
        return "\n".join(rec)

class AgricultureSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Agriculture Management System")
        self.farm_manager = FarmManager()
        self.setup_gui()

    def setup_gui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.add_crop_frame = ttk.Frame(self.notebook)
        self.view_crops_frame = ttk.Frame(self.notebook)
        self.insights_frame = ttk.Frame(self.notebook)
        self.help_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.add_crop_frame, text="Add Crop")
        self.notebook.add(self.view_crops_frame, text="View Crops")
        self.notebook.add(self.insights_frame, text="Insights")
        self.notebook.add(self.help_frame, text="Help")

        self.setup_add_crop()
        self.setup_view_crops()
        self.setup_insights()
        self.setup_help()

    def setup_add_crop(self):
        ttk.Label(self.add_crop_frame, text="Crop Name:").grid(row=0, column=0, padx=5, pady=5)
        self.crop_name_combo = ttk.Combobox(self.add_crop_frame, values=list(Crop.CROP_INFO.keys()))
        self.crop_name_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.add_crop_frame, text="Planting Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.planting_date_entry = ttk.Entry(self.add_crop_frame)
        self.planting_date_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.add_crop_frame, text="Soil Quality:").grid(row=2, column=0, padx=5, pady=5)
        self.soil_quality_combo = ttk.Combobox(self.add_crop_frame, values=["Good", "Average", "Poor"])
        self.soil_quality_combo.grid(row=2, column=1, padx=5, pady=5)
        self.soil_quality_combo.set("Average")

        ttk.Label(self.add_crop_frame, text="Weather Forecast:").grid(row=3, column=0, padx=5, pady=5)
        self.weather_combo = ttk.Combobox(self.add_crop_frame, values=["Favorable", "Moderate", "Harsh"])
        self.weather_combo.grid(row=3, column=1, padx=5, pady=5)
        self.weather_combo.set("Moderate")

        ttk.Label(self.add_crop_frame, text="Health Status:").grid(row=4, column=0, padx=5, pady=5)
        self.health_combo = ttk.Combobox(self.add_crop_frame, values=["Healthy", "Stressed"])
        self.health_combo.grid(row=4, column=1, padx=5, pady=5)
        self.health_combo.set("Healthy")

        ttk.Label(self.add_crop_frame, text="Soil Type:").grid(row=5, column=0, padx=5, pady=5)
        self.soil_type_combo = ttk.Combobox(self.add_crop_frame, values=["Loamy", "Clayey", "Sandy"])
        self.soil_type_combo.grid(row=5, column=1, padx=5, pady=5)
        self.soil_type_combo.set("Loamy")

        ttk.Label(self.add_crop_frame, text="Land Area (Hectares):").grid(row=6, column=0, padx=5, pady=5)
        self.land_area_entry = ttk.Entry(self.add_crop_frame)
        self.land_area_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Button(self.add_crop_frame, text="Add Crop", command=self.submit_crop).grid(row=7, column=0, columnspan=2, pady=10)

    def submit_crop(self):
        try:
            name = self.crop_name_combo.get()
            planting_date = datetime.strptime(self.planting_date_entry.get(), "%Y-%m-%d")
            soil_quality = self.soil_quality_combo.get()
            weather_condition = self.weather_combo.get()
            health_status = self.health_combo.get()
            soil_type = self.soil_type_combo.get()
            land_area = float(self.land_area_entry.get())
            if not name:
                messagebox.showerror("Error", "Please select a crop")
                return
            if land_area <= 0:
                messagebox.showerror("Error", "Land area must be positive")
                return
            crop = Crop(name, planting_date, soil_quality, weather_condition, health_status, soil_type, land_area)
            self.farm_manager.add_crop(crop)
            messagebox.showinfo("Success", f"Crop {name} added!")
        except ValueError as e:
            messagebox.showerror("Error", str(e) or "Invalid date format. Use YYYY-MM-DD")

    def setup_view_crops(self):
        columns = ("Name", "Stage", "Soil Quality", "Weather", "Health", "Soil Type", "Land Area")
        self.tree = ttk.Treeview(self.view_crops_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(self.view_crops_frame, text="Refresh Crops", command=self.refresh_crops).grid(row=1, column=0, pady=5)

    def refresh_crops(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        crops = self.farm_manager.get_crops()
        for crop in crops:
            crop.update_growth_stage()
            self.tree.insert("", tk.END, values=(crop.name, crop.growth_stage, crop.soil_quality,
                                               crop.weather_condition, crop.health_status, crop.soil_type, crop.land_area))

    def setup_insights(self):
        self.insights_text = tk.Text(self.insights_frame, height=15, width=60)
        self.insights_text.grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(self.insights_frame, text="Show Summary", command=self.show_summary).grid(row=1, column=0, pady=5, sticky="w")
        ttk.Button(self.insights_frame, text="Predict Yield", command=self.show_yield).grid(row=1, column=0, pady=5, sticky="n")
        ttk.Button(self.insights_frame, text="Recommendations", command=self.show_recommendations).grid(row=1, column=0, pady=5, sticky="e")
        ttk.Button(self.insights_frame, text="Export Recommendations", command=self.export_recommendations).grid(row=2, column=0, pady=5)

    def show_summary(self):
        self.insights_text.delete(1.0, tk.END)
        crops = self.farm_manager.get_crops()
        if not crops:
            self.insights_text.insert(tk.END, "No crops added yet.")
            return
        total_crops = len(crops)
        total_area = sum(crop.land_area for crop in crops)
        avg_yield = round(sum(Insights.predict_yield(crop) for crop in crops) / total_crops, 2)
        total_cost = sum(crop.get_info()["total_cost"] * crop.land_area for crop in crops)
        water_needs = [crop.get_info()["water_needs"][crop.growth_stage] for crop in crops]
        self.insights_text.insert(tk.END, f"Total Crops: {total_crops}\n"
                                        f"Total Area: {total_area:.2f} hectares\n"
                                        f"Average Yield: {avg_yield}/100\n"
                                        f"Total Investment: ₹{total_cost:,}\n"
                                        f"Water Needs: {', '.join(set(water_needs))}\n")

    def show_yield(self):
        self.insights_text.delete(1.0, tk.END)
        crops = self.farm_manager.get_crops()
        if not crops:
            self.insights_text.insert(tk.END, "No crops to predict yield for.")
            return
        for crop in crops:
            yield_amount = Insights.predict_yield(crop)
            self.insights_text.insert(tk.END, f"Predicted Yield for {crop.name}: {yield_amount}/100\n")

    def show_recommendations(self):
        self.insights_text.delete(1.0, tk.END)
        crops = self.farm_manager.get_crops()
        if not crops:
            self.insights_text.insert(tk.END, "No crops to provide recommendations for.")
            return
        for crop in crops:
            rec = Insights.get_recommendations(crop)
            self.insights_text.insert(tk.END, f"Recommendations for {crop.name}:\n{rec}\n\n")

    def export_recommendations(self):
        crops = self.farm_manager.get_crops()
        if not crops:
            messagebox.showerror("Error", "No crops to export recommendations for.")
            return
        with open("crop_recommendations.txt", "w", encoding="utf-8") as f:
            for crop in crops:
                rec = Insights.get_recommendations(crop)
                f.write(f"Recommendations for {crop.name}:\n{rec}\n\n")
        messagebox.showinfo("Success", "Recommendations exported to crop_recommendations.txt")

    def setup_help(self):
        self.help_text = tk.Text(self.help_frame, height=15, width=60)
        self.help_text.grid(row=0, column=0, padx=5, pady=5)
        help_content = (
            "Welcome to the Digital Agriculture Management System!\n\n"
            "Base Yield Explanation:\n"
            "- Base yield is the expected yield per hectare out of 100 units under ideal conditions.\n"
            "- It varies by crop (e.g., Sugarcane: 90/100, Tea: 60/100) based on Indian agricultural productivity.\n"
            "- Adjusted by soil quality (+20%/-20%), weather (+30%/-30%), health (-10% if stressed), and soil type (+10%/-10%).\n"
            "- Example: Rice (85/100) with good soil, favorable weather, healthy status, and loamy soil yields 85 * 1.2 * 1.3 * 1.1 = 145.86/100 (capped at 100).\n\n"
            "Costs in INR:\n"
            "- Includes seeds, fertilizers, labor, irrigation, and pesticides.\n"
            "- Total cost is calculated based on land area (hectares).\n"
            "- Example: 2 ha of Rice at ₹40,000/ha = ₹80,000 total.\n\n"
            "How to Use:\n"
            "- Add Crop: Select crop, enter planting date, conditions, and land area.\n"
            "- View Crops: Refresh to see all crops in a table.\n"
            "- Insights: View summary, yields, or recommendations.\n"
            "- Export: Save recommendations to a text file."
        )
        self.help_text.delete(1.0, tk.END)
        self.help_text.insert(tk.END, help_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgricultureSystemGUI(root)
    root.mainloop()