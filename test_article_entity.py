# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest
from article_entity.article_entity import article_entity, _split_title, _guess_contain, _keep_item


@pytest.mark.parametrize('title,content,expected', [
    ('', '', []),
    (
        '这是一个简单的测试',
        """The human soul has still greater need of the ideal than of the real.
        It is by the real that we exist; it is by the ideal that we live. —Victor Hugo 测试""",
        ['测试']
    ),

    (
        '可购物视频平台 Packagd 完成KPCB领投的A轮600万美元融资 ',
        """近日，移动视频商业化平台 Packagd 宣布完成 600万美元的 A轮融资，领投方为 KPCB（凯鹏华盈），至此该公司的融资总额达到了 750万美元。与此同时 Packagd 推出了其第一款应用程序 Unboxed，展示最热门的技术产品、小工具和设备。

        Packagd 是一家位于硅谷的创业公司，由 KPCB 孵化，Kleiner Perkins 合伙人 Eric Feng，Nick Chang，Larry Chen，Eden Li，以及 Kai Ju Liu 于 2016年联合创办，旨在为一系列应用程序提供视频平台，为消费者带来全新的移动购物体验。

        Packagd 联合创始人兼首席执行官 Eric Feng 表示：“在电视时代，‘电商即娱乐’这一理念帮助 HSN 和 QVC 这样的传统企业建立了数十亿美元的商业帝国。 使用视频来推动商业并不是一个全新概念，但是 Packagd 有机会将这种体验带给新一代移动消费者。”

        近些年来“开箱视频”呈现出明显的上涨趋势，越来越多的内容创作者开始对产品做出测评，在全球范围内，开箱视频的观看次数已经超过了 100亿次，其中 62%的观看者会有潜在的购买行为。

        尽管开箱视频如此火爆，但 Packagd 是第一个利用其中潜在零售机会的公司。基于发现、社区和商务的核心理念，Packagd 的应用程序通过专家策划的产品展示，帮助消费者通过真实的评论认识新产品，通过即时聊天与主持人和其他观众互动，还能通过 Apple Pay 在应用程序内部完成购买。""",
        ['Packagd'],
    ),

    (
        '苹果设计师竟是猫奴？为猫设计专属音箱',
        """6月6号凌晨的苹果全球开发者大会在高考的巨大声势下显得有点悄无声息。这场在库克口中“最大最好的WWDC”到底有什么独特魅力，租机姐姐从中选取了几点来为大家介绍介绍。
        iOS 11
        不知道有没有小伙伴跟租机姐姐一样，嫌麻烦从不升级系统，其实在配置允许的情况下，系统的升级会更好的表现产品的性能。
        iOS 11对于iOS 10，首先最直观的变化就是外观上的变化。
        可以看出iOS11的控制中心从从 iOS 10 的卡片式变成了类似气泡的式样，并且可以实现编辑的功能，用户可以根据自己的使用习惯进行编辑，不得不说还是十分方便的。
        在支付宝和微信支付如此普及的中国，14年苹果推出的Apple pay实在是翻不起多大的水花。在iOS 11中，Apple pay总算是可以转账了，你可以在iMessage 里和别人进行现金的转账，功能相当于微信红包。
        虽然功能比微信支付宝落后了很多，但租机姐姐觉得Apple pay真的很方便，靠近有银联闪付标志的读卡器，就可以直接进行指纹支付，不用解除锁屏，也不用打开app，除了覆盖率太低之外没毛病。
        很多爱拍照的小伙伴可能都会面对一个相同的问题，内存不足。作为一个曾经的16G用户，租机姐姐手机里的APP是能少则少，相册里照片是精挑细选删了又删，跟同事表情包斗图再也没赢过。最后还是屈服换了64G，然而现在64G的容量也有点捉襟见肘，只怪自己爱自拍。
        iOS 11用 HEIF 照片格式代替了 JPG，照片的文件体积可以缩小到一半；用 HEVC 格式的 H.265 编码替代了现在的 H.264 视频格式，视频的格式也可以缩小到原来的一半。对于内存不足的用户可以说是火中送碳了。
        此外，iOS 11的相机还增加了不少新功能，例如二维码扫描，不管是什么样的二维码都可以直接用相机进行扫描，免去打开APP的步骤。还可以自动生成长曝光照片，可以让照片里的溪水变成丝稠状，让路上的车灯拖成光带。
        安全一直都是让人十分瞩目的问题，租机姐姐曾经遇到过一个出租车司机边看电视剧边开车，最近重庆一司机被曝出边开车边斗地主，租机姐姐不禁佩服老司机车技好。开车时候分心是非常危险的行为，一不小心就会酿成大祸。
        iOS 11加入了针对开车的一项安全功能：驾驶勿扰模式。iPhone 会根据你 Wifi、蓝牙和陀螺仪的工作状态来推断你是不是在开车，一旦确认，就会把你的手机完全黑屏，同时不显示任何通知。等你停下车，才会集中弹出刚才错过的事件。
        租机姐姐觉得现在社会手机成瘾的现象越来越严重，很多人开车也不忘发发微信抢抢红包，是不小的安全隐患，苹果的这个功能，可以说是非常实用了。
        和过去一样，苹果单独为中国区开发了几个特有功能，有垃圾短信屏蔽、上海话 Siri、拼音键盘英文混输、电话号码作为 Apple ID 账号等等。
        上海话Siri这两天也是刷爆了朋友圈，租机姐姐表示热烈欢迎，就是不知道识别率如何，也希望苹果公司继续努力，中国大大小小几十种方言等待你。
        HomePod 智能音箱
        传了一年多的 Siri 智能音响在WWDC上发布，最终被命名为 HomePod。
        对于养猫的租机姐姐来说，看到这款音箱的第一感觉是，我家猫一定很喜欢。
        外形宛如卷纸和毛线球的HomePod，不知道是不是为了让猫远离键盘而故意设计成这样的，如果是的话，说不定可以大大提高有猫人士在家的办公效率呢。
        2400RMB的价格，这可能是猫玩过的最贵的玩具。
        但是现在的这些都还没有正式上线，等秋季苹果公司就会正式来收割你们的肾了。没钱的小伙伴们可以来快租365租一台体验最新的苹果产品~ """,
        ['苹果'],
    ),

    (
        '苹果设计师竟是猫奴？为猫设计专属音箱',
        """6月6号凌晨的苹果全球开发者大会在高考的巨大声势下显得有点悄无声息。这场在库克口中“最大最好的WWDC”到底有什么独特魅力，租机姐姐从中选取了几点来为大家介绍介绍。
        iOS 11
        不知道有没有小伙伴跟租机姐姐一样，嫌麻烦从不升级系统，其实在配置允许的情况下，系统的升级会更好的表现产品的性能。
        iOS 11对于iOS 10，首先最直观的变化就是外观上的变化。
        可以看出iOS11的控制中心从从 iOS 10 的卡片式变成了类似气泡的式样，并且可以实现编辑的功能，用户可以根据自己的使用习惯进行编辑，不得不说还是十分方便的。
        在支付宝和微信支付如此普及的中国，14年苹果推出的Apple pay实在是翻不起多大的水花。在iOS 11中，Apple pay总算是可以转账了，你可以在iMessage 里和别人进行现金的转账，功能相当于微信红包。
        虽然功能比微信支付宝落后了很多，但租机姐姐觉得Apple pay真的很方便，靠近有银联闪付标志的读卡器，就可以直接进行指纹支付，不用解除锁屏，也不用打开app，除了覆盖率太低之外没毛病。
        很多爱拍照的小伙伴可能都会面对一个相同的问题，内存不足。作为一个曾经的16G用户，租机姐姐手机里的APP是能少则少，相册里照片是精挑细选删了又删，跟同事表情包斗图再也没赢过。最后还是屈服换了64G，然而现在64G的容量也有点捉襟见肘，只怪自己爱自拍。""",
        ['苹果'],
    ),

    (
        '医疗健康领域共享社区Figure1完成B轮融资，被称为医生版Instagram',
        """
        医疗领域共享平台Figure1被称为医生版的Instagram，36氪获悉，成立四年的Figure1现在已经拥有超过200万注册用户，其中有一百多万医疗专家在Figure1上分享有关罕见病例、新型治疗方案的图片和文字信息。
        医疗健康领域共享社区Figure1完成B轮融资，被称为医生版Instagram
        医疗领域共享平台Figure1被称为医生版的Instagram，36氪获悉，成立四年的Figure1现在已经拥有超过200万注册用户，其中有一百多万医疗专家在Figure1上分享有关罕见病例、新型治疗方案的图片和文字信息。

        Figure1从创立之初就颇受资本青睐，加上最近由Kensington Capital Partners领投的1000万美元的B轮融资，Figure1已累计获得超过两千万美元的融资。在国内，类似的社区平台“医学界”、“医生汇”等也相继获得融资，相信Figure1的发展模式和运营理念会给国内创业者带来一些启发。

        虽然总部在加拿大多伦多，Figure1的会员却有三分之二来自美国，在拉丁美洲也有很大的用户量。作为专业型分享平台，Figure1也对医疗专家以外的普通用户开放，其中包括医学院学生以及医学门外汉，只不过非专业用户只能在平台上浏览信息而不能发言。

        Figure1没有将平台定位于医疗健康领域中某个垂直细分场景，而在一开始就向整个医疗健康领域开放，这个策略现在看来卓有成效，来自医疗健康各领域的用户贡献着自己的内容，让平台自发而有机地成长。

        和众多线上分享社区一样，如何鼓励用户发言也是Figure1需要应对的问题，对此，Figure1的总裁Gregory Levey 认为：“一个社区中只有少部分人发言其实很正常，Figure1不强求每个用户必须发言，只希望大家可以在平台上获得自己认为有价值的东西。”

        同时，Figure1也在避免自己成为一个媒体，因为在Figure1看来，对于医疗健康领域来说，打造一个让用户自发分享、创造价值的可持续社区比做一个媒体更有价值。
        """,
        ['Figure1'],
    ),

])
def test_article_entity(title, content, expected):
    assert expected == article_entity(title, content)


@pytest.mark.parametrize('title,expected', [
    ('测试English Test', ['测', '试', 'English', ' ', 'Test']),
    ('测试English2 Test', ['测', '试', 'English', '2', ' ', 'Test']),
])
def test_split_title(title, expected):
    assert expected == _split_title(title)


@pytest.mark.parametrize('key,dict,expected', [
    ('aa', dict(aa=1, aabbcc=1), True),
    ('aa', dict(abc=2, aabbcc=1, aa=1, bb=1, cc=1), True),
    ('aa', dict(aa=1, aabbcc=2), False),
    ('aa', dict(aa=1), False),
    ('aa', dict(aa=1, bb=2), False),
])
def test_guess_contain(key, dict, expected):
    assert expected == _guess_contain(key, dict)


@pytest.mark.parametrize('key,dict,expected', [
    # number
    ('11', {'11': 'whatever value'}, False),
    (11, {11: 'whatever value'}, False),
])
def test_keep_item(key, dict, expected):
    assert expected == _keep_item(key, dict)
