## Commune

Commune is an internal tool for managing communities using Discord.

You will be able to track engagement metrics, schedule events and messages, and
more. We will be providing data integrations for you to export the data you need.

## Development Progress

At the moment, we are integrating support for Discord.

- Event
- Message Scheduling
- Engagement Metrics

## License

MIT License


## 2023.06.20 新增需求

- 考量到擴充性及機制可能還會不斷變動，STS 希望可以在小工具編輯以下內容：
    - 訊息內容（可能有 default 內容，但期待可以手動變更裡面部分文字）
    - 發送時間（不同活動有不同的提醒頻率）
    - 發送頻道（頻道未來可能還會有多次修改的需求）
- 介面需求：
    - 目前小工具為助教 Q&A 提醒寄送介面，期待一種活動類型有一個獨立介面，分開管理及客製化訊息、寄送頻率
    - 期待可以在介面上看到詳細資訊，包括最終呈現的訊息內容、寄送頻道、寄送時間等，以確認設定是否正確
- 理想流程：
    - STS 確認活動時間後，交由 intern / pt 登錄 dashboard
    - intern / pt 至小工具按照不同活動類別，分別登錄接下來一個月的活動
    - 不同活動可依照 STS 指定的頻率發送提醒，例如：
        - 助教 Q&A：每週週一
        - 工作坊：前一週及當天
        - …
