import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Geo, Timeline, Grid
from pyecharts.globals import ChartType
from pyecharts.faker import Faker
import datetime

data = pd.read_excel('*/path.xlsx')
dummy = pd.read_excel('*/dummy.xlsx')

plane = "path:///M 763.6 270.4 L 181.2 71.6 c -15.1 -5.1 -30.2 -2.4 -39.8 7.2 l -16.7 16.7 s 235.6 149.8 449.8 364 c 170.2 170.2 364 449.8 364 449.8 l 16.7 -16.7 c 9.6 -9.6 12.3 -24.7 7.2 -39.8 L 763.6 270.4 Z M 347 687 L 60.1 640.8 c -8.2 -0.5 -17.7 3.8 -25.2 11.3 l -13 13 s 115.4 48.8 206.8 140.2 c 72.5 72.5 140.2 206.8 140.2 206.8 l 13 -13 c 7.5 -7.5 11.7 -17 11.3 -25.2 L 347 687 Z""path://M 962.4 852.8 L 763.6 270.4 L 574.5 459.5 c 170.2 170.2 364 449.8 364 449.8 l 16.7 -16.7 c 9.7 -9.6 12.4 -24.7 7.2 -39.8 Z M 393.2 973.9 L 347 687 L 228.8 805.2 C 301.4 877.8 369 1012 369 1012 l 13 -13 c 7.3 -7.4 11.6 -17 11.2 -25.1 Z""path://M 892.6 291.5 L 463.8 720.3 C 422.3 761.8 126.4 990.5 85 949 c -41.4 -41.4 187.3 -337.3 228.7 -378.8 l 428.8 -428.8 C 783.9 100 936.9 14.2 978.3 55.7 c 41.5 41.4 -44.3 194.4 -85.7 235.8 Z""path://M 898.8 220.9 l -85.7 -85.7 l 75 -46.5 l 57.2 57.2 Z""path://M 855.9 178.1 l 42.9 42.8 l 46.5 -75 l -28.6 -28.6 Z"
train = "path://M362 287C357.587 287.014 354.014 290.587 354 295L354 341C354.01 344.309 356.691 346.99 360 347L396 347C399.309 346.989 401.989 344.309 402 341L402 295C401.986 290.587 398.413 287.014 394 287ZM400 297 400 320 356 320 356 297 374 297 374 296C374 295.448 374.448 295 375 295L381 295C381.552 295 382 295.448 382 296L382 297ZM396 345 360 345C357.792 344.997 356.003 343.208 356 341L356 322 400 322 400 341C399.997 343.208 398.208 344.997 396 345ZM400 295 383.831 295C383.405 293.802 382.272 293.001 381 293L375 293C373.729 293.002 372.596 293.802 372.171 295L356 295C356.004 291.688 358.688 289.004 362 289L394 289C397.312 289.004 399.996 291.688 400 295Z""path://M363 334C360.791 334 359 335.791 359 338 359 340.209 360.791 342 363 342 365.209 342 367 340.209 367 338 367.023 335.814 365.27 334.023 363.084 334 363.056 334 363.028 334 363 334ZM363 340C361.895 340 361 339.105 361 338 361 336.895 361.895 336 363 336 364.105 336 365 336.895 365 338 365.025 339.08 364.169 339.975 363.089 340 363.059 340.001 363.03 340.001 363 340Z""path://M393 334C390.791 334 389 335.791 389 338 389 340.209 390.791 342 393 342 395.209 342 397 340.209 397 338 397.023 335.814 395.27 334.023 393.084 334 393.056 334 393.028 334 393 334ZM393 340C391.895 340 391 339.105 391 338 391 336.895 391.895 336 393 336 394.105 336 395 336.895 395 338 395.025 339.08 394.169 339.975 393.089 340 393.059 340.001 393.03 340.001 393 340Z""path://M392.709 350 394.064 353 361.936 353 363.291 350 361.1 350 349.355 376 351.549 376 353.807 371 402.193 371 404.451 376 406.645 376 394.9 350ZM401.29 369 354.71 369 357.42 363 398.58 363ZM397.677 361 358.323 361 361.033 355 394.968 355Z"

tl = Timeline()
dum = []
p = list(set(data['date']))
p.sort()

### plot travel trail
for i in p:
    a = np.where(data['date'] == i)
    loc_list = []

    for k in range(0, a[0][0]):
        b = (data['location1'][k], data['location2'][k])
        loc_list.append(b)

    location_list = np.unique(loc_list).tolist()

    c = (
        Geo()
        .add_schema(maptype="china",
                    itemstyle_opts=opts.ItemStyleOpts(color='#323c48', border_color='#404a59'),
                    label_opts=opts.LabelOpts(is_show=True, color="grey"))
        .add("geo",
             loc_list,
             type_=ChartType.LINES,
             symbol_size=5,
             effect_opts=opts.EffectOpts(
                 symbol_size=2, color="#1F8D59", trail_length=0.2
             ),
             linestyle_opts=opts.LineStyleOpts(curve=0.2, color="#2CCA7F", width=1, type_="dashed"),
             label_opts=opts.LabelOpts(is_show=False, position="middle", color="#1F8D59"),
             )
        .add("geo",
             [(data.loc[data['date'] == i, 'location1'].values.item(),
               data.loc[data['date'] == i, 'location2'].values.item())],
             type_=ChartType.LINES,
             symbol_size=10,
             effect_opts=opts.EffectOpts(
                 symbol=plane, color="#3A83B0", symbol_size=30, trail_length=0.03
             ),
             linestyle_opts=opts.LineStyleOpts(curve=0.2, color="#2CCA7F", width=1, type_="solid"),
             label_opts=opts.LabelOpts(is_show=False, position="middle", color="#1F8D59"),
             )
        .add("",
             [("上海", "Home Office")],
             type_=ChartType.EFFECT_SCATTER,
             color="#7AE2B0",
             label_opts=opts.LabelOpts(is_show=False)
             )
        .set_global_opts(title_opts=opts.TitleOpts(title="行程轨迹图"))
    )

    tl.add(c, i)

### plot expense details in location points
for o in list(set(location_list)):
    c = c.add("",
              [(o, dum)],
              type_=ChartType.SCATTER,
              color="#FFFFFF",
              label_opts=opts.LabelOpts(is_show=False),
              tooltip_opts=opts.TooltipOpts(formatter=dummy[dummy['location'] == o].to_html()))
tl.add(c, i)

tl.add_schema(axis_type='time', orient='horizontal', symbol='circle', symbol_size=10,
              play_interval=1000, is_auto_play=True, is_loop_play=False, is_timeline_show=True)

tl.render("map.html")
