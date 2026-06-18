-- Custom Signals: one subgroup + the v1 train-station virtual signals.
-- Display names live in locale/en/custom-signals.cfg, matched by `name`.
-- Icon files live in graphics/icons/<name>.png at 64x64.

local function station_signal(name, order)
  return {
    type = "virtual-signal",
    name = name,
    icon = "__custom-virtual-signals__/graphics/icons/" .. name .. ".png",
    icon_size = 64,
    subgroup = "custom-signals-stations",
    order = order,
  }
end

data:extend({
  {
    type = "item-subgroup",
    name = "custom-signals-stations",
    group = "signals",
    order = "zzz-custom-signals-a",
  },
  station_signal("cs-requester-station", "a"),
  station_signal("cs-provider-station", "b"),
  station_signal("cs-depot-station", "c"),
  station_signal("cs-refuel-station", "d"),
})
