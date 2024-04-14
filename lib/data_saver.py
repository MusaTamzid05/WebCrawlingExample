import pandas as pd
import os

class DataSaver:
    def __init__(self, data):
        self.data = data

    def start(self):
        normal_data_list = []
        coordinate_data_list = []
        review_data_list = []
        comfort_data_list = []

        for row in self.data:
            try:
                normal_data = {}
                normal_data["product_id"] = row["product_id"]
                normal_data["product_url"] = row["product_url"]
                normal_data["image_urls"] = ",".join(row["image_urls"])
                normal_data["breadcrumb_categories"] = row["breadcrumb_categories"]
                normal_data["sizes"] = ",".join(row["sizes"])
                normal_data["category_name"] = row["category_name"]
                normal_data["sence_of_size"] = row["sence_of_size"]
                normal_data["title"] = row["basic_info"]["title"]
                normal_data["price"] = row["basic_info"]["price"]

                if len(row["coordinates"]) > 0:
                    coordinate_data = {}
                    for coordinate_row in row["coordinates"]:
                        coordinate_data["title"] = coordinate_row["title"]
                        coordinate_data["src_product_url"] = row["product_url"]
                        coordinate_data["url"] = coordinate_row["url"]
                        coordinate_data["image_url"] = coordinate_row["image_url"]
                        coordinate_data["price"] = coordinate_row["price"]
                        coordinate_data_list.append(coordinate_data)

                if "inner_data" in row:

                    normal_data["title_of_description"] = row["inner_data"]["heading"]
                    normal_data["general_description"] = row["inner_data"]["description"]
                    normal_data["description_itemization"] = ",".join(row["inner_data"]["points"])

                if "chart_size" in row:
                    normal_data["tall_of_size"] = row["chart_size"]
                
                normal_data["KWS"] = row["KWS"]

                if "ratting" in row:
                    normal_data["user_ratting"] = row["ratting"]["user_ratting"]
                    normal_data["user_ratting_count"] = row["ratting"]["user_count"]
                    normal_data["user_ratting_percentage"] = row["ratting"]["percentage"]
                else:
                    normal_data["user_ratting"] = "N/A"
                    normal_data["user_ratting_count"] = "N/A"
                    normal_data["user_ratting_percentage"] = "N/A"



                normal_data_list.append(normal_data)

                if "reviews" in row:

                    for review in row["reviews"]:
                        review_data = {}
                        review_data["product_url"] = row["product_url"]
                        review_data["title"] = review["title"]
                        review_data["text"] = review["text"]
                        review_data["username"] = review["username"]
                        review_data["date"] = review["date"]
                        review_data["review_ratting"] = review["review_ratting"]

                        review_data_list.append(review_data)

                if "scene_of_comforts" in row:
                    for comfort in row["scene_of_comforts"]:
                        comfort_data = {}
                        comfort_data["product_url"] = row["product_url"]
                        comfort_data["min"] = comfort["min"]
                        comfort_data["max"] = comfort["max"]
                        comfort_data["title"] = comfort["title"]


                        comfort_data_list.append(comfort_data)

            except Exception as e:
                print(f"Error saving data row => {e}")


        #print(normal_data_list)
        #print(coordinate_data_list)
        #print(review_data_list)
        #print(comfort_data_list)

        self.save_excel(
                normal_data_list=normal_data_list,
                coordinate_data_list=coordinate_data_list,
                review_data_list=review_data_list,
                comfort_data_list=comfort_data_list
                )

    def save_excel(
            self,
            normal_data_list,
            coordinate_data_list,
            review_data_list,
            comfort_data_list
            ):

        output_path = "./output.xlsx"
        df_normal = pd.DataFrame(normal_data_list)
        df_coordinates = pd.DataFrame(coordinate_data_list)
        df_review = pd.DataFrame(review_data_list)
        df_comfort_data = pd.DataFrame(comfort_data_list)



        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:

            df_normal.to_excel(writer, sheet_name='NormalData',  index=False)
            df_coordinates.to_excel(writer, sheet_name='Coordinates', index=False)
            df_review.to_excel(writer, sheet_name='Reviews', index=False)
            df_comfort_data.to_excel(writer, sheet_name='Comfort',  index=False)












if __name__ == "__main__":
    results = [{'product_id': 'IA4877', 'product_url': 'https://shop.adidas.jp/products/IA4877/', 'image_urls': ['https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-on_model-standard_view-R2Ts1qqN5B.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-71-I6i8jB8c0H.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-72-e93bcnyJmz.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-on_model-back_view-UIag7LoRRW.jpg'], 'breadcrumb_categories': 'トップ   /   メンズ   /   ウェア・服   /   トップス   /   Tシャツ   /   オリジナルス   /   アディカラー   /   アディカラー クラシック   /   アディカラー クラシックス スリーストライプス 長袖Tシャツ', 'sizes': ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'], 'category_name': 'メンズオリジナルス', 'sence_of_size': '3.0', 'basic_info': {'title': 'アディカラー クラシックス スリーストライプス 長袖Tシャツ', 'price': '5,500'}, 'coordinates': [{'url': 'https://shop.adidas.jp/products/EG4959', 'image_url': 'https://shop.adidas.jp/photo/EG/EG4959/s-EG4959-standard-side_lateral_view.jpg', 'title': 'スーパースター / Superstar', 'price': '10,890'}], 'inner_data': {'description': 'クラシックアイテムをアップデートした、存在感のあるシグネチャースタイルが誕生。このコントラストの効いたアディダスの長袖Tシャツで颯爽と出かけよう。今どきのレトロな雰囲気を漂わせたアイコニックなスリーストライプスと、刺しゅうのトレフォイルがポイント。さらに、リブ仕上げのクルーネックと袖口を採用し、全体をクラシックにまとめている。', 'heading': 'スリーストライプスが目を引く、快適な長袖Tシャツ。', 'points': ['スリムフィット', 'リブ編みのクルーネック', 'コットン100%（シングルジャージー）', 'リブ仕上げのカフ', 'ベターコットンを使用', '商品番号：IA4877', '色：ブラック', '生産国：Pakistan,Vietnam']}, 'chart_size': {'胸囲': {'XS': '90cm', 'S': '93cm', 'M': '98cm', 'L': '100cm', 'XL': '105cm', '2XL': '111cm', '3XL': '118cm'}, 'うしろ着丈': {'XS': '67cm', 'S': '68cm', 'M': '69cm', 'L': '69cm', 'XL': '70cm', '2XL': '72cm', '3XL': '73cm'}, '袖丈': {'XS': '77cm', 'S': '77cm', 'M': '77cm', 'L': '78cm', 'XL': '78cm', '2XL': '79cm', '3XL': '79cm'}, '袖口幅': {'XS': '24cm', 'S': '25cm', 'M': '25cm', 'L': '25cm', 'XL': '26cm', '2XL': '27cm', '3XL': '28cm'}}, 'KWS': 'ウェア・服,トップス,Tシャツ,オリジナルス,アディカラー,クラシックス,スリー ストライプス,アディカラー クラシック,長袖,ベターコットン,BVB94', 'ratting': {'user_ratting': '4.6', 'user_count': '10', 'percentage': '100%'}, 'reviews': [{'title': '’７０年代を思い起こすデザイン～即買い！！', 'review_ratting': '4 / 5', 'text': ' ’70年～’80年のadidasデザインな好きな私には、最高の商品です！サイズ感は、168cm71㌔の私にはMサイズは、ぴったりフィット感です\n', 'username': 'FunkySeven ', 'date': '2024年1月17日'}, {'title': '不変のデザイン', 'review_ratting': '5 / 5', 'text': ' 時代や流行が関係ないデザインで長く着用できそうです。素材感も柔らかく着心地がいいです。パジャマとしてきても心地よいですね。\n', 'username': 'kaminarikozou ', 'date': '2023年12月2日'}, {'title': 'タイトな作り？', 'review_ratting': '4 / 5', 'text': ' 若干タイト目なつくりなのか普段よりワンサイズアップでもジャストフィットでした。ゆるめに着たい方は2サイズくらいあげてもいいかも\n', 'username': 'vgyu ', 'date': '2023年5月21日'}, {'title': 'クラシックなデザインがいい', 'review_ratting': '4 / 5', 'text': ' いつもより良いワンサイズアップで購入しましたが、ちょうどいいサイズでした。袖の3本線、リンガーネックがクラシックでいい感じです。袖口のリブがルーズなのはちょっと嫌かな。でも、色違いも欲しいです。\n', 'username': 'moddie ', 'date': '2024年3月13日'}, {'title': 'シルエット', 'review_ratting': '5 / 5', 'text': ' 他の方のレビューてはタイトと記載があったが、そんなにタイトではなかった。通常のサイズ選びで大丈夫てす。\n', 'username': 'tomorrow ', 'date': '2024年1月26日'}, {'title': 'デザイン、機能性抜群です', 'review_ratting': '5 / 5', 'text': ' どのようなパンツでも合わせやすく、着こごち良く、洗濯しても首周りがしっかりしてて満足してます。配送スピードもあり、梱包もとても丁寧です。\n', 'username': 'hankabu ', 'date': '2023年5月15日'}, {'title': '', 'review_ratting': '4 / 5', 'text': ' シルエットが素晴らしいサイズもバランス良くできてる普段着でバシバシ着たいと思います新作がでたら買いたい\n', 'username': 'nao555 ', 'date': '2024年2月26日'}, {'title': 'シルエットがとても素敵です。', 'review_ratting': '5 / 5', 'text': ' １５６センチ４８キロ女性です。袖は少し長いですが、ベージュに黒３本線、何にでも合わせることができます。普段着にもいいかも。\n', 'username': 'my29 ', 'date': '2023年9月22日'}, {'title': '最近のadidasはタイトな造りが多い気がする', 'review_ratting': '5 / 5', 'text': ' The adidas Oliginals的なアパレルを買いたいと思っていたところ、店舗でこちらの商品を見つけました。adidasでは旧サイズ感のXOを着るので、今回もXXL（現O）を着てみたところ、少しタイトでした。オンラインでXXXLを取り寄せてみたところ、自分の好きなサイズ感でした。こちらのカラーとブラックの2枚を購入して、大満足です。身長183cm、体重74kgの男性レビューです。\n', 'username': 'TokyoCustomMade ', 'date': '2023年3月8日'}, {'title': '好きなデザイン', 'review_ratting': '5 / 5', 'text': ' ネットで見ていたら一目惚れして購入しました。ちょうど整体で着る長袖のシャツを探してたので良い買い物をした気分です。\n', 'username': 'jizou ', 'date': '2023年7月29日'}], 'scene_of_comforts': [{'min': 'タイトすぎる', 'max': 'ルーズすぎる', 'title': '2.8 / 5'}, {'min': '短すぎる', 'max': '長すぎる', 'title': '2.8 / 5'}, {'min': '低い', 'max': '高い', 'title': '3.7 / 5'}, {'min': '全く快適ではない', 'max': 'とても快適', 'title': '4 / 5'}]}, {'product_id': 'IA4846', 'product_url': 'https://shop.adidas.jp/products/IA4846/', 'image_urls': ['https://shop.adidas.jp/photo/IA/IA4846/z-IA4846-on_model-standard_view-3tkmSqEhNf.jpg', 'https://shop.adidas.jp/photo/IA/IA4846/z-IA4846-71-TxLhqzGVao.jpg', 'https://shop.adidas.jp/photo/IA/IA4846/z-IA4846-72-KzUtNpbKIC.jpg', 'https://shop.adidas.jp/photo/IA/IA4846/z-IA4846-73-LUZRy0J4kD.jpg'], 'breadcrumb_categories': 'トップ   /   メンズ   /   ウェア・服   /   トップス   /   Tシャツ   /   オリジナルス   /   アディカラー   /   アディカラー クラシック   /   アディカラー クラシックス スリーストライプス Tシャツ', 'sizes': ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'], 'category_name': 'メンズオリジナルス', 'sence_of_size': '3.5', 'basic_info': {'title': 'アディカラー クラシックス スリーストライプス Tシャツ', 'price': '4,400'}, 'coordinates': [], 'inner_data': {'description': '新たなお気に入りになりそうな、着心地の良いコットンTシャツ。スリムフィットな作りにコントラストカラーの裾をあしらった、洗練されたビンテージ感漂うデザインが特徴。お気に入りのダークデニムと合わせれば、クラシックコーデもお手の物。素材には、快適な着心地を生むとびきりソフトなコットンを採用している。サステナブルな綿花栽培をサポートしている、アディダスのコットン製品。', 'heading': 'コーディネートしやすい、汎用性のあるクラシックTシャツ。', 'points': ['スリムフィット', 'リブ編みのクルーネック', 'コットン100%（シングルジャージー）', 'リブ仕上げのカフ', 'ベターコットンを使用', '商品番号：IA4846', '色：ホワイト', '生産国：China,Indonesia,Pakistan']}, 'chart_size': {'胸囲': {'XS': '90cm', 'S': '93cm', 'M': '98cm', 'L': '100cm', 'XL': '105cm', '2XL': '111cm', '3XL': '118cm'}, 'うしろ着丈': {'XS': '67cm', 'S': '68cm', 'M': '69cm', 'L': '69cm', 'XL': '70cm', '2XL': '72cm', '3XL': '73cm'}, '袖丈': {'XS': '34cm', 'S': '35cm', 'M': '36cm', 'L': '36cm', 'XL': '37cm', '2XL': '39cm', '3XL': '41cm'}}, 'KWS': 'ウェア・服,トップス,Tシャツ,オリジナルス,アディカラー,クラシックス,スリー ストライプス,MINI ME（ミニミー）,アディカラー クラシック,半袖,ベターコットン,BVB48', 'ratting': {'user_ratting': '4.8', 'user_count': '22', 'percentage': '100%'}, 'reviews': [{'title': '体操着', 'review_ratting': '4 / 5', 'text': ' 白のTシャツの手持ちが少なく体操着っぽいので迷っていましたがブレイキンの上位選手が着ていたのでスポーツ用として白を購入。レディースのように首回りがボディと同じ色のものも出して欲しいです。\n', 'username': 'messiah ', 'date': '2024年3月10日'}, {'title': '綺麗なイエロー', 'review_ratting': '5 / 5', 'text': ' このタイプのTシャツはこのイエローは綺麗な色味だったので気分も上がると思い購入 レーディスを試着したがピッタリするのでメンズのMにした最適 グッド\n', 'username': 'Yugary88 ', 'date': '2024年4月6日'}, {'title': '鮮やかな色', 'review_ratting': '5 / 5', 'text': ' それぞれの季節に合う色がとても嬉しい。各色揃えて楽しんでます。着心地や色の明るさがとても良いから毎年楽しみです。\n', 'username': 'namakurakatana ', 'date': '2024年4月13日'}, {'title': '色違いで何枚も', 'review_ratting': '5 / 5', 'text': ' 174cm/3XL黒と白を持っているので今回は半袖を購入。いつものサイズである2XLが売り切れだったので3XLを購入しましたが大きめの可愛さがあっめこれはこれで良かったです。\n', 'username': 'S1986 ', 'date': '2023年12月19日'}, {'title': 'デザインがかわいあ', 'review_ratting': '5 / 5', 'text': ' 白黒が流行っていましたがこの色を着てる方を見たことがないので被らなくてかわいいです。あと、ゆったりしすぎず、ぴったりしすぎずちょうどいいサイズ感でした。\n', 'username': 'rippe ', 'date': '2024年1月9日'}, {'title': 'かわいすき゛た！', 'review_ratting': '4 / 5', 'text': ' 黒を選んだのが正解すぎるくらいシルエットも着心地も最高可愛すぎる！ダボッと着るよりは少しぴちっとしたサイズのがかわいいとおもった\n', 'username': 'harpmusic ', 'date': '2024年2月7日'}, {'title': 'いい感じ‼︎', 'review_ratting': '5 / 5', 'text': ' ジムでのトレーニング用に赤のTシャツが欲しくて買いました。丈が少し長めですが鮮やかな赤色で気に入ってます。\n', 'username': 'v126v ', 'date': '2023年10月16日'}, {'title': '大満足です。', 'review_ratting': '5 / 5', 'text': ' XLサイズを購入しましたがインナーにも重ね着にも使えて重宝しています。またKing Gnuの常田大希さんが以前YouTubeに上がっているadidasの動画内で着用していたためファンの方は購入必須だと思います。\n', 'username': 'Kieven ', 'date': '2023年12月10日'}, {'title': '満足です', 'review_ratting': '5 / 5', 'text': ' 白、黒、赤と購入しましたが赤が一番お気に入りです。白とのコントラストがキレイです。着心地もいいです。\n', 'username': 'Linn ', 'date': '2024年1月31日'}, {'title': 'Tシャツ界のスターかもしれない', 'review_ratting': '5 / 5', 'text': ' 着てよし 質よし かっこよし。Tシャツとしては気持ち高めなこととスポーツフィールドでの使用想定感が購入前の印象だったが、いざ、着てみると街に遊びに行ったりするのにも違和感なく、幅広い能力があることを知ることが出来た。まだ知らない方には、大いにお勧めしたい。\n', 'username': 'lucky7878 ', 'date': '2024年1月26日'}], 'scene_of_comforts': [{'min': 'タイトすぎる', 'max': 'ルーズすぎる', 'title': '3 / 5'}, {'min': '短すぎる', 'max': '長すぎる', 'title': '3.3 / 5'}, {'min': '低い', 'max': '高い', 'title': '4.3 / 5'}, {'min': '全く快適ではない', 'max': 'とても快適', 'title': '4.4 / 5'}]}, {'product_id': 'IU2341', 'product_url': 'https://shop.adidas.jp/products/IU2341/', 'image_urls': ['https://shop.adidas.jp/photo/IU/IU2341/z-IU2341-on_model-standard_view-DnJ8fHQEbD.jpg', 'https://shop.adidas.jp/photo/IU/IU2341/z-IU2341-on_model-back_view-OtmggPL601.jpg', 'https://shop.adidas.jp/photo/IU/IU2341/z-IU2341-on_model-walking_view-EwT1sqwsCd.jpg', 'https://shop.adidas.jp/photo/IU/IU2341/z-IU2341-3d_torso-front_center_view-DRtO3vjBJ5.jpg'], 'breadcrumb_categories': 'トップ   /   メンズ   /   ウェア・服   /   トップス   /   Tシャツ   /   オリジナルス   /   アディカラー   /   アディカラー 半袖Tシャツ', 'sizes': ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'], 'category_name': 'メンズオリジナルス', 'sence_of_size': 'No sence of size', 'basic_info': {'title': 'アディカラー 半袖Tシャツ', 'price': '6,600'}, 'coordinates': [{'url': 'https://shop.adidas.jp/products/FY7755', 'image_url': 'https://shop.adidas.jp/photo/FY/FY7755/s-FY7755-standard-side_lateral_view.jpg', 'title': 'フォーラム ロー / FORUM LOW', 'price': '12,100'}, {'url': 'https://shop.adidas.jp/products/IT2501', 'image_url': 'https://shop.adidas.jp/photo/IT/IT2501/s-IT2501-73-yPj4CJIhxl.jpg', 'title': 'アディカラー ウーブン ファイヤーバードトラックパンツ（ジャージ）', 'price': '12,100'}], 'inner_data': {'description': 'このアディダスTシャツは、ワードローブの必需品。ゆったりとしたシルエットだから、オフの日にはジョガーパンツと、夜の外出にはデニムと合わせたりしてみよう。クラシックなジャージーにインスパイアされた、スポーティーな雰囲気のデザイン。アディダスのDNAを受け継ぐ、アイコニックなトレフォイルを正面にフィーチャー。 この製品には、リサイクル素材を70%以上使用。製造された製品の素材をリユースするが、ゴミの量、限りある資源への依存、そしてアディダス製品のフットプリントを減らすことにつながる。', 'heading': 'リサイクル素材を一部使用したデイリーTシャツ。', 'points': ['ルーズフィット', 'リブ仕上げのクルーネック', 'ポリエステル100%（ジャカード）', '商品番号：IU2341', '色：ブラック/ホワイト']}, 'chart_size': {'胸囲': {'XS': '102cm', 'S': '105cm', 'M': '110cm', 'L': '112cm', 'XL': '117cm', '2XL': '123cm', '3XL': '130cm'}, 'うしろ着丈': {'XS': '67cm', 'S': '68cm', 'M': '69cm', 'L': '69cm', 'XL': '70cm', '2XL': '72cm', '3XL': '73cm'}, '袖丈': {'XS': '19cm', 'S': '19cm', 'M': '20cm', 'L': '20cm', 'XL': '21cm', '2XL': '22cm', '3XL': '23cm'}}, 'KWS': 'ウェア・服,トップス,Tシャツ,オリジナルス,アディカラー,半袖,リサイクル素材一部使用,KMA93', 'ratting': {'user_ratting': '5', 'user_count': '2', 'percentage': '100%'}, 'reviews': [{'title': 'ユニークなデザイン、女性の私にとってとても美しいです', 'review_ratting': '5 / 5', 'text': ' このシャツは本当に気に入っています、クールで私のスタイルにとてもよく合っています. 友達全員に買ったのですが、みんなとても気に入ってくれました\n', 'username': 'Zanzan ', 'date': '2024年4月3日'}, {'title': '狙った通りのシルエット', 'review_ratting': '5 / 5', 'text': ' 自分は172センチ 67キロ テニスを割とやっていて肩幅広めホワイトのXLを購入ルーズフィット目にして、下にロンTきたり、薄手のパーカーを合わせようとしてこのサイズに。狙い通りのシルエットができました。肩が落ちているデザインで、縦のストライプが写真のように入っているのが気に入ったのと、アディダスのトレフォイルマークが入っているコットン生地タイプのＴシャツは多いのですが、これは100%ポリエステル生地のＴシャツってかなりレアで、この光沢感はポリエステルならではですね。一枚で着てもスケ感がないのも気に入っています。\n（非表示）', 'username': 'JAM1008 ', 'date': '2024年4月1日'}], 'scene_of_comforts': [{'min': 'タイトすぎる', 'max': 'ルーズすぎる', 'title': '3 / 5'}, {'min': '短すぎる', 'max': '長すぎる', 'title': '3 / 5'}, {'min': '低い', 'max': '高い', 'title': '4 / 5'}, {'min': '全く快適ではない', 'max': 'とても快適', 'title': '3.5 / 5'}]}, {'product_id': 'IM0410', 'product_url': 'https://shop.adidas.jp/products/IM0410/', 'image_urls': ['https://shop.adidas.jp/photo/IM/IM0410/z-IM0410-on_model-standard_view-j7ce0fe96N.jpg', 'https://shop.adidas.jp/photo/IM/IM0410/z-IM0410-on_model-back_view-ShHA3E3vEZ.jpg', 'https://shop.adidas.jp/photo/IM/IM0410/z-IM0410-on_model-walking_view-hqFrXSJflF.jpg', 'https://shop.adidas.jp/photo/IM/IM0410/z-IM0410-3d_torso-front_center_view-z2kthStxyk.jpg'], 'breadcrumb_categories': 'トップ   /   メンズ   /   ウェア・服   /   トップス   /   Tシャツ   /   オリジナルス   /   アディカラー   /   アディカラー クラシック   /   アディカラー クラシックス スリーストライプス Tシャツ', 'sizes': ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'], 'category_name': 'メンズオリジナルス', 'sence_of_size': '3.5', 'basic_info': {'title': 'アディカラー クラシックス スリーストライプス Tシャツ', 'price': '4,400'}, 'coordinates': [{'url': 'https://shop.adidas.jp/products/GX9753', 'image_url': 'https://shop.adidas.jp/photo/GX/GX9753/s-GX9753-standard-side_lateral_view.jpg', 'title': 'スタンスミスADV / Stan SmithADV', 'price': '13,200'}], 'inner_data': {'description': '新たなお気に入りになりそうな、着心地の良いコットンTシャツ。スリムフィットな作りにコントラストカラーの裾をあしらった、洗練されたビンテージ感漂うデザインが特徴。お気に入りのダークデニムと合わせれば、クラシックコーデもお手の物。素材には、快適な着心地を生むとびきりソフトなコットンを採用している。サステナブルな綿花栽培をサポートしている、アディダスのコットン製品。', 'heading': 'コーディネートしやすい、汎用性のあるクラシックTシャツ。', 'points': ['スリムフィット', 'リブ編みのクルーネック', 'コットン100%（シングルジャージー）', 'リブ仕上げのカフ', 'ベターコットンを使用', '商品番号：IM0410', '色：グリーン', '生産国：Pakistan']}, 'chart_size': {'胸囲': {'XS': '90cm', 'S': '93cm', 'M': '98cm', 'L': '100cm', 'XL': '105cm', '2XL': '111cm', '3XL': '118cm'}, 'うしろ着丈': {'XS': '67cm', 'S': '68cm', 'M': '69cm', 'L': '69cm', 'XL': '70cm', '2XL': '72cm', '3XL': '73cm'}, '袖丈': {'XS': '34cm', 'S': '35cm', 'M': '36cm', 'L': '36cm', 'XL': '37cm', '2XL': '39cm', '3XL': '41cm'}}, 'KWS': 'ウェア・服,トップス,Tシャツ,オリジナルス,アディカラー,クラシックス,スリー ストライプス,MINI ME（ミニミー）,アディカラー クラシック,半袖,ベターコットン,BVB48', 'ratting': {'user_ratting': '4.8', 'user_count': '22', 'percentage': '100%'}, 'reviews': [{'title': '体操着', 'review_ratting': '4 / 5', 'text': ' 白のTシャツの手持ちが少なく体操着っぽいので迷っていましたがブレイキンの上位選手が着ていたのでスポーツ用として白を購入。レディースのように首回りがボディと同じ色のものも出して欲しいです。\n', 'username': 'messiah ', 'date': '2024年3月10日'}, {'title': '綺麗なイエロー', 'review_ratting': '5 / 5', 'text': ' このタイプのTシャツはこのイエローは綺麗な色味だったので気分も上がると思い購入 レーディスを試着したがピッタリするのでメンズのMにした最適 グッド\n', 'username': 'Yugary88 ', 'date': '2024年4月6日'}, {'title': '鮮やかな色', 'review_ratting': '5 / 5', 'text': ' それぞれの季節に合う色がとても嬉しい。各色揃えて楽しんでます。着心地や色の明るさがとても良いから毎年楽しみです。\n', 'username': 'namakurakatana ', 'date': '2024年4月13日'}, {'title': '色違いで何枚も', 'review_ratting': '5 / 5', 'text': ' 174cm/3XL黒と白を持っているので今回は半袖を購入。いつものサイズである2XLが売り切れだったので3XLを購入しましたが大きめの可愛さがあっめこれはこれで良かったです。\n', 'username': 'S1986 ', 'date': '2023年12月19日'}, {'title': 'デザインがかわいあ', 'review_ratting': '5 / 5', 'text': ' 白黒が流行っていましたがこの色を着てる方を見たことがないので被らなくてかわいいです。あと、ゆったりしすぎず、ぴったりしすぎずちょうどいいサイズ感でした。\n', 'username': 'rippe ', 'date': '2024年1月9日'}, {'title': 'かわいすき゛た！', 'review_ratting': '4 / 5', 'text': ' 黒を選んだのが正解すぎるくらいシルエットも着心地も最高可愛すぎる！ダボッと着るよりは少しぴちっとしたサイズのがかわいいとおもった\n', 'username': 'harpmusic ', 'date': '2024年2月7日'}, {'title': 'いい感じ‼︎', 'review_ratting': '5 / 5', 'text': ' ジムでのトレーニング用に赤のTシャツが欲しくて買いました。丈が少し長めですが鮮やかな赤色で気に入ってます。\n', 'username': 'v126v ', 'date': '2023年10月16日'}, {'title': '大満足です。', 'review_ratting': '5 / 5', 'text': ' XLサイズを購入しましたがインナーにも重ね着にも使えて重宝しています。またKing Gnuの常田大希さんが以前YouTubeに上がっているadidasの動画内で着用していたためファンの方は購入必須だと思います。\n', 'username': 'Kieven ', 'date': '2023年12月10日'}, {'title': '満足です', 'review_ratting': '5 / 5', 'text': ' 白、黒、赤と購入しましたが赤が一番お気に入りです。白とのコントラストがキレイです。着心地もいいです。\n', 'username': 'Linn ', 'date': '2024年1月31日'}, {'title': 'Tシャツ界のスターかもしれない', 'review_ratting': '5 / 5', 'text': ' 着てよし 質よし かっこよし。Tシャツとしては気持ち高めなこととスポーツフィールドでの使用想定感が購入前の印象だったが、いざ、着てみると街に遊びに行ったりするのにも違和感なく、幅広い能力があることを知ることが出来た。まだ知らない方には、大いにお勧めしたい。\n', 'username': 'lucky7878 ', 'date': '2024年1月26日'}], 'scene_of_comforts': [{'min': 'タイトすぎる', 'max': 'ルーズすぎる', 'title': '3 / 5'}, {'min': '短すぎる', 'max': '長すぎる', 'title': '3.3 / 5'}, {'min': '低い', 'max': '高い', 'title': '4.3 / 5'}, {'min': '全く快適ではない', 'max': 'とても快適', 'title': '4.4 / 5'}]}, {'product_id': 'IA4877', 'product_url': 'https://shop.adidas.jp/products/IA4877/', 'image_urls': ['https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-on_model-standard_view-R2Ts1qqN5B.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-71-I6i8jB8c0H.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-72-e93bcnyJmz.jpg', 'https://shop.adidas.jp/photo/IA/IA4877/z-IA4877-on_model-back_view-UIag7LoRRW.jpg'], 'breadcrumb_categories': 'トップ   /   メンズ   /   ウェア・服   /   トップス   /   Tシャツ   /   オリジナルス   /   アディカラー   /   アディカラー クラシック   /   アディカラー クラシックス スリーストライプス 長袖Tシャツ', 'sizes': ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'], 'category_name': 'メンズオリジナルス', 'sence_of_size': '3.0', 'basic_info': {'title': 'アディカラー クラシックス スリーストライプス 長袖Tシャツ', 'price': '5,500'}, 'coordinates': [{'url': 'https://shop.adidas.jp/products/EG4959', 'image_url': 'https://shop.adidas.jp/photo/EG/EG4959/s-EG4959-standard-side_lateral_view.jpg', 'title': 'スーパースター / Superstar', 'price': '10,890'}], 'inner_data': {'description': 'クラシックアイテムをアップデートした、存在感のあるシグネチャースタイルが誕生。このコントラストの効いたアディダスの長袖Tシャツで颯爽と出かけよう。今どきのレトロな雰囲気を漂わせたアイコニックなスリーストライプスと、刺しゅうのトレフォイルがポイント。さらに、リブ仕上げのクルーネックと袖口を採用し、全体をクラシックにまとめている。', 'heading': 'スリーストライプスが目を引く、快適な長袖Tシャツ。', 'points': ['スリムフィット', 'リブ編みのクルーネック', 'コットン100%（シングルジャージー）', 'リブ仕上げのカフ', 'ベターコットンを使用', '商品番号：IA4877', '色：ブラック', '生産国：Pakistan,Vietnam']}, 'chart_size': {'胸囲': {'XS': '90cm', 'S': '93cm', 'M': '98cm', 'L': '100cm', 'XL': '105cm', '2XL': '111cm', '3XL': '118cm'}, 'うしろ着丈': {'XS': '67cm', 'S': '68cm', 'M': '69cm', 'L': '69cm', 'XL': '70cm', '2XL': '72cm', '3XL': '73cm'}, '袖丈': {'XS': '77cm', 'S': '77cm', 'M': '77cm', 'L': '78cm', 'XL': '78cm', '2XL': '79cm', '3XL': '79cm'}, '袖口幅': {'XS': '24cm', 'S': '25cm', 'M': '25cm', 'L': '25cm', 'XL': '26cm', '2XL': '27cm', '3XL': '28cm'}}, 'KWS': 'ウェア・服,トップス,Tシャツ,オリジナルス,アディカラー,クラシックス,スリー ストライプス,アディカラー クラシック,長袖,ベターコットン,BVB94', 'ratting': {'user_ratting': '4.6', 'user_count': '10', 'percentage': '100%'}, 'reviews': [{'title': '’７０年代を思い起こすデザイン～即買い！！', 'review_ratting': '4 / 5', 'text': ' ’70年～’80年のadidasデザインな好きな私には、最高の商品です！サイズ感は、168cm71㌔の私にはMサイズは、ぴったりフィット感です\n', 'username': 'FunkySeven ', 'date': '2024年1月17日'}, {'title': '不変のデザイン', 'review_ratting': '5 / 5', 'text': ' 時代や流行が関係ないデザインで長く着用できそうです。素材感も柔らかく着心地がいいです。パジャマとしてきても心地よいですね。\n', 'username': 'kaminarikozou ', 'date': '2023年12月2日'}, {'title': 'タイトな作り？', 'review_ratting': '4 / 5', 'text': ' 若干タイト目なつくりなのか普段よりワンサイズアップでもジャストフィットでした。ゆるめに着たい方は2サイズくらいあげてもいいかも\n', 'username': 'vgyu ', 'date': '2023年5月21日'}, {'title': 'クラシックなデザインがいい', 'review_ratting': '4 / 5', 'text': ' いつもより良いワンサイズアップで購入しましたが、ちょうどいいサイズでした。袖の3本線、リンガーネックがクラシックでいい感じです。袖口のリブがルーズなのはちょっと嫌かな。でも、色違いも欲しいです。\n', 'username': 'moddie ', 'date': '2024年3月13日'}, {'title': 'シルエット', 'review_ratting': '5 / 5', 'text': ' 他の方のレビューてはタイトと記載があったが、そんなにタイトではなかった。通常のサイズ選びで大丈夫てす。\n', 'username': 'tomorrow ', 'date': '2024年1月26日'}, {'title': 'デザイン、機能性抜群です', 'review_ratting': '5 / 5', 'text': ' どのようなパンツでも合わせやすく、着こごち良く、洗濯しても首周りがしっかりしてて満足してます。配送スピードもあり、梱包もとても丁寧です。\n', 'username': 'hankabu ', 'date': '2023年5月15日'}, {'title': '', 'review_ratting': '4 / 5', 'text': ' シルエットが素晴らしいサイズもバランス良くできてる普段着でバシバシ着たいと思います新作がでたら買いたい\n', 'username': 'nao555 ', 'date': '2024年2月26日'}, {'title': 'シルエットがとても素敵です。', 'review_ratting': '5 / 5', 'text': ' １５６センチ４８キロ女性です。袖は少し長いですが、ベージュに黒３本線、何にでも合わせることができます。普段着にもいいかも。\n', 'username': 'my29 ', 'date': '2023年9月22日'}, {'title': '最近のadidasはタイトな造りが多い気がする', 'review_ratting': '5 / 5', 'text': ' The adidas Oliginals的なアパレルを買いたいと思っていたところ、店舗でこちらの商品を見つけました。adidasでは旧サイズ感のXOを着るので、今回もXXL（現O）を着てみたところ、少しタイトでした。オンラインでXXXLを取り寄せてみたところ、自分の好きなサイズ感でした。こちらのカラーとブラックの2枚を購入して、大満足です。身長183cm、体重74kgの男性レビューです。\n', 'username': 'TokyoCustomMade ', 'date': '2023年3月8日'}, {'title': '好きなデザイン', 'review_ratting': '5 / 5', 'text': ' ネットで見ていたら一目惚れして購入しました。ちょうど整体で着る長袖のシャツを探してたので良い買い物をした気分です。\n', 'username': 'jizou ', 'date': '2023年7月29日'}], 'scene_of_comforts': [{'min': 'タイトすぎる', 'max': 'ルーズすぎる', 'title': '2.8 / 5'}, {'min': '短すぎる', 'max': '長すぎる', 'title': '2.8 / 5'}, {'min': '低い', 'max': '高い', 'title': '3.7 / 5'}, {'min': '全く快適ではない', 'max': 'とても快適', 'title': '4 / 5'}]}]
    data_saver = DataSaver(data=results)
    data_saver.start()

